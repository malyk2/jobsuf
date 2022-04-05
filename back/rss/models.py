from django.db import models
from django.contrib.postgres.functions import RandomUUID
import uuid
# Create your models here.

# class Country(models.Model):
#     name = models.CharField(max_length=255, blank=False)
#     created = models.DateTimeField(auto_now_add=True)


TYPE_CHOICES = [
    ('topics', 'topics'),
    ('jobs', 'jobs'),
]

TOPIC_CHOICES = [
    ('most-recent', 'most-recent'),
    ('best-matches', 'best-matches'),
]


class Upwork(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(choices=TYPE_CHOICES,
                            blank=False, max_length=100)
    topic = models.CharField(choices=TOPIC_CHOICES, null=True, max_length=100)
    q = models.CharField(blank=True, max_length=100)
    active = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    user = models.ForeignKey(
        'auth.User', related_name='rss', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Secret(models.Model):
    org_uid = models.CharField(max_length=100, blank=False)
    security_token = models.CharField(max_length=200, blank=False)
    user_uid = models.CharField(max_length=100, blank=False)

    user = models.OneToOneField(
        'auth.User', related_name='rss_secret', on_delete=models.CASCADE)


class Country(models.Model):
    name = models.CharField(max_length=255, blank=False)
    created = models.DateTimeField(auto_now_add=True)


class Job(models.Model):
    # id = models.UUIDField(primary_key= True, default=RandomUUID)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=True, default='')
    content = models.TextField(null=True)
    upwork_id = models.CharField(max_length=255, null=True, default='')
    rate_from = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    rate_to = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    budget = models.PositiveSmallIntegerField(null=True)
    published = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(
        'rss.Country', related_name='jobs', null=True, on_delete=models.SET_NULL)
    rss = models.ForeignKey(
        'rss.Upwork', related_name='jobs', null=True, on_delete=models.SET_NULL)
    readed_users = models.ManyToManyField(
        'auth.User', related_name='readed_rss_jobs')
    favourited_users = models.ManyToManyField(
        'auth.User', related_name='favourited_rss_jobs', through='JobFavouritedUsers')


class Skill(models.Model):
    name = models.CharField(max_length=255, blank=False)
    jobs = models.ManyToManyField(Job, related_name='skills')


class JobFavouritedUsers(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    group = models.ForeignKey(Job, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    rate = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'rss_job_favourited_users'
