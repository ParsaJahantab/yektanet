from django.urls import path
from .views import *

urlpatterns = [
    path('users/applicants/', ApplicantCreateView.as_view()),
    path('users/applicants/<int:pk>/', ApplicantRetrieveView.as_view()),
    path('users/interviewers/', InterviewerCreateView.as_view()),
    path('users/interviewers/<int:pk>', InterviewerRetrieveView.as_view()),
    path('interviews/', InterviewCreateView.as_view()),
    path('interviews/<int:pk>', InterviewerRetrieveView.as_view()),
    path('users/access/interviewers/interviews/', InterviewForInterviewerListView.as_view()),
    path('users/access/interviewers/applicants/', ApplicantForInterviewerListView.as_view()),
    path('users/access/interviewrs/create/feedback/<int:pk>', FeedbackCreateAPI.as_view()),
    path('users/access/interviewrs/create/comment/<int:pk>', CommentCreateAPI.as_view()),
    path('users/telegram/<str:username>/<int:chat_id>',telegram),
    path('test/',test),
    path('user/check/', check),

]
