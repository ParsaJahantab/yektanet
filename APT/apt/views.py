from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response

from .serializer import *
from .permission import IsHRPermission, AccessToInterview

from .tasks import send_timed_massage,task_test
from datetime import datetime, timedelta

class ApplicantCreateView(generics.ListCreateAPIView):
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return (permissions.IsAuthenticated(), IsHRPermission())


class ApplicantRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return (permissions.IsAuthenticated(), IsHRPermission())


class InterviewerCreateView(generics.ListCreateAPIView):
    serializer_class = InterviewerSerializer
    queryset = Interviewer.objects.all()
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return (permissions.IsAuthenticated(), IsHRPermission())


class InterviewerRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interviewer.objects.all()
    serializer_class = InterviewerSerializer
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return (permissions.IsAuthenticated(), IsHRPermission())


class InterviewCreateView(generics.ListCreateAPIView):
    serializer_class = InterviewSerializer
    queryset = Interview.objects.all()
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return (permissions.IsAuthenticated(), IsHRPermission())


class InterviewRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InterviewSerializer
    queryset = Interview.objects.all()
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return (permissions.IsAuthenticated(), IsHRPermission())


def check(request):
    authentication_classes = (
        TokenAuthentication,
    )
    return HttpResponse(request.user)


class InterviewForInterviewerListView(generics.ListAPIView):
    serializer_class = InterviewSerializer
    # queryset = Interview.objects.all()
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return (permissions.IsAuthenticated(), AccessToInterview())

    def get_queryset(self):
        user = self.request.user
        interviewer = user.interviewer
        queryset = Interview.objects.filter(interviewer=interviewer)
        if len(queryset) == 0:
            return self.permission_denied(self.request)
        else:
            return queryset
        # return Interview.objects.filter(interviewer=interviewer)


class ApplicantForInterviewerListView(generics.ListAPIView):
    serializer_class = InterviewApplicantSerializer
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return (permissions.IsAuthenticated(), AccessToInterview())

    def get_queryset(self):
        user = self.request.user
        interviewer = user.interviewer
        queryset = Interview.objects.filter(interviewer=interviewer)
        if len(queryset) == 0:
            return self.permission_denied(self.request)
        else:
            return queryset
        # return Interview.objects.filter(interviewer=interviewer)


class FeedbackCreateAPI(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
    authentication_classes = (
        TokenAuthentication,
    )

    def get_queryset(self):
        user = self.request.user
        interviewer = user.interviewer
        queryset = Interview.objects.filter(interviewer=interviewer)
        if len(queryset) == 0:
            return self.permission_denied(self.request)
        else:
            return queryset
        # return Interview.objects.filter(interviewer=interviewer)
    def get_permissions(self):
        return (permissions.IsAuthenticated(), AccessToInterview())

    def perform_create(self, serializer):
        instance = self.get_object()
        serializer.save(interview=instance)


class CommentCreateAPI(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    authentication_classes = (
        TokenAuthentication,
    )

    def get_queryset(self):
        user = self.request.user
        interviewer = user.interviewer
        queryset = Interview.objects.filter(interviewer=interviewer)
        if len(queryset) == 0:
            return self.permission_denied(self.request)
        else:
            return queryset
        # return Interview.objects.filter(interviewer=interviewer)

    def get_permissions(self):
        return (permissions.IsAuthenticated(), AccessToInterview())

    def perform_create(self, serializer):
        instance = self.get_object()
        serializer.save(interview=instance)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(queryset=Comment.objects.filter(interview=self.get_object()))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    def print(self):
        print('hello world')
@api_view(('GET',))
#@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def telegram(request,username,chat_id):
    #applicant :Applicant = Applicant.objects.get(pk=1)
    queryset=Applicant.objects.filter(telegram_id=username)
    applicant :Applicant = Applicant.objects.filter(telegram_id=username)[0]
    applicant.chat_id = chat_id
    # print(chat_id)
    # print(applicant)
    # print(applicant.chat_id)
    applicant.save()

    # try:
    #     applicat = Applicant.objects.filter(telegram_id=username)[0]
    # except:
    #     return Response(status=418)
    interview :Interview = Interview.objects.filter(applicant = applicant)[0]
    #interview:Interview = applicant.interview_applicant
    print(type(interview))
    date = interview.date
    time_to_execute = date-timedelta(hours=1)
    print(time_to_execute)
    print(date)
    send_timed_massage.apply_async((chat_id,applicant.name,date),eta=time_to_execute)

    return Response(data=date,status=201)


def test(request):
    print(datetime.now())

    time_to_execute = datetime.now() +timedelta(seconds=20)
    print(time_to_execute)
    task_test.apply_async(eta=time_to_execute)




