# Generated by Django 4.1 on 2022-08-28 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apt', '0003_applicant_name_interview_applicant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='interview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_interview', to='apt.interview'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='interview',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='interview_feedback', to='apt.interview'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interview_applicant', to='apt.applicant'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='interviewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interview_interviewer', to='apt.interviewer'),
        ),
    ]
