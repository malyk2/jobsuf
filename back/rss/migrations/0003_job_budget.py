# Generated by Django 4.0.3 on 2022-03-25 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0002_job_readed_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='budget',
            field=models.IntegerField(null=True),
        ),
    ]
