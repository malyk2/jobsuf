# Generated by Django 4.0.3 on 2022-03-23 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Upwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('type', models.CharField(choices=[('topic', 'topic'), ('job', 'job')], max_length=100)),
                ('topic', models.CharField(choices=[('most-recent', 'most-recent'), ('best-matches', 'best-matches')], max_length=100, null=True)),
                ('q', models.CharField(blank=True, max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_uid', models.CharField(max_length=100)),
                ('security_token', models.CharField(max_length=200)),
                ('user_uid', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rss_secret', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]