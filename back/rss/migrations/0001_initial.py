# Generated by Django 4.0.3 on 2022-03-24 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255, null=True)),
                ('content', models.TextField(null=True)),
                ('upwork_id', models.CharField(default='', max_length=255, null=True)),
                ('rate_from', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('rate_to', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('published', models.DateTimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country', to='rss.country')),
            ],
        ),
        migrations.CreateModel(
            name='Upwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('type', models.CharField(choices=[('topics', 'topics'), ('jobs', 'jobs')], max_length=100)),
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
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('jobs', models.ManyToManyField(related_name='skills', to='rss.job')),
            ],
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
        migrations.AddField(
            model_name='job',
            name='rss',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rss', to='rss.upwork'),
        ),
    ]
