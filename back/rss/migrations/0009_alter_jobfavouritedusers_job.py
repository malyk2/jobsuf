# Generated by Django 4.0.3 on 2022-06-23 18:41

from django.db import migrations, models
import django.db.models.deletion
from django.contrib.postgres.operations import HStoreExtension


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0008_rename_group_jobfavouritedusers_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobfavouritedusers',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pivot_favourited_users', to='rss.job'),
        ),
    ]
