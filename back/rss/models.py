from django.db import models
from django.contrib.postgres.functions import RandomUUID

# Create your models here.

# class Country(models.Model):
#     name = models.CharField(max_length=255, blank=False)
#     created = models.DateTimeField(auto_now_add=True)


TYPE_CHOICES = [
    ('topic', 'topic'),
    ('job', 'job'),
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
    id = models.UUIDField(primary_key= True, auto_created=True, default=RandomUUID)
    title = models.CharField(max_length=255, null=True, default='')
    content = models.TextField(null=True)
    upwork_id = models.CharField(max_length=255, null=True, default='')
    rate_from = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    rate_to = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    published = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(
        'rss.Country', related_name='country', null=True, on_delete=models.SET_NULL)
    rss = models.ForeignKey(
        'rss.Upwork', related_name='rss', null=True, on_delete=models.SET_NULL)
