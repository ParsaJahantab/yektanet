from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *
from django.contrib.auth import get_user_model


class ApplicantSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200, write_only=True)
    password = serializers.CharField(max_length=200, write_only=True)

    def save(self, **kwargs):
        user_model = get_user_model()
        username = self.validated_data.pop('username')
        password = self.validated_data.pop('password')
        user = user_model.objects.create_user(username=username, password=password, )
        token = Token.objects.create(user=user)
        applicant = super().save(user=user, **kwargs)
        return applicant

    class Meta:
        model = Applicant
        fields = (
            'username',
            'password',
            'name',
            'resume',
            'linkedin_address',
            'age',
            'sex',
            'status'
        )


class InterviewerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200,write_only=True)
    password = serializers.CharField(max_length=200,write_only=True)
    def save(self, **kwargs):
        user_model = get_user_model()
        username = self.validated_data.pop('username')
        password = self.validated_data.pop('password')
        user = user_model.objects.create_user(username=username, password=password, )
        token = Token.objects.create(user=user)
        interviewer = super().save(user=user, **kwargs)
        return interviewer

    class Meta:
        model = Interviewer
        fields = (
            'username',
            'password',
        )


class InterviewSerializer(serializers.ModelSerializer):
    interviewer = InterviewerSerializer(read_only=True)
    applicant = ApplicantSerializer(read_only=True)
    date = serializers.DateTimeField()

    class Meta:
        model = Interview
        fields = (
            'interview_type',
            'interviewer',
            'applicant',
            'date'
        )

class InterviewApplicantSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(read_only=True)
    class Meta:
        model = Interview
        fields = (
            'applicant',
        )

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'comment_text',
        )


class FeedbackSerializer(serializers.ModelSerializer):
    #interview = InterviewSerializer(read_only=True)


    class Meta:
        model = Feedback
        fields = (
            'feedback_text',
        )
