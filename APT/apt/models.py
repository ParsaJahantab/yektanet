from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    telegram_id = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100 , null=True)
    resume = models.TextField(null=True)
    linkedin_address = models.URLField(null=True)
    age = models.PositiveIntegerField(default=0)
    chat_id = models.IntegerField(editable=False,null=True)
    sex_choices = (
        ('male', 'M'),
        ('female', 'F'),
    )
    sex = models.CharField(max_length=100, choices=sex_choices,default='M')
    status_choices = (
        ('pending', 'P'),
        ('confirmed', 'C'),
        ('failed', 'F'),
    )
    status = models.CharField(max_length=100, choices=status_choices,default='P')


class HR(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Interviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Interview(models.Model):
    createdat = models.DateTimeField(auto_now=True)
    date = models.DateTimeField()
    interview_types = [
        ('phone', 'P'),
        ('tech', 'T'),
        ('code', 'C'),
        ('final', 'F'),
    ]
    interview_type = models.CharField(max_length=100, choices=interview_types)
    interviewer = models.ForeignKey(Interviewer,on_delete=models.CASCADE,null=True,related_name='interview_interviewer')
    applicant = models.ForeignKey(Applicant,on_delete=models.CASCADE,null=True,related_name='interview_applicant')






class Comment(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE,related_name='comment_interview')
    comment_text = models.TextField()


class Feedback(models.Model):
    feedback_text = models.TextField()
    interview = models.OneToOneField(Interview, on_delete=models.CASCADE,related_name='interview_feedback')
