# Generated by Django 4.1 on 2022-08-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apt', '0004_alter_comment_interview_alter_feedback_interview_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='createdat',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
