# Generated by Django 4.0.3 on 2022-03-25 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0004_jobfavouritedusers_job_favourited_users_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='jobfavouritedusers',
            table='rss_job_favourited_users',
        ),
    ]
