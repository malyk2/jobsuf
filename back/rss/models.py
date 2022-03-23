from django.db import models

# Create your models here.

# class Country(models.Model):
#     name = models.CharField(max_length=255, blank=False)
#     created = models.DateTimeField(auto_now_add=True)

# class Jobs(models.Model):
# #     Country
# # content
# # published
#     title = models.CharField(max_length=255, blank=True, default='')
#     content = models.TextField(blank=True)
#     upwork_id = models.CharField(max_length=255, blank=True, default='')
#     published = models.DateTimeField(blank=True)
#     country = models.ForeignKey('rss.Country', related_name='country', on_delete=models.SET_NULL)
#     created = models.DateTimeField(auto_now_add=True)

#     # rss = models.ForeignKey('user_rss.Country', related_name='country', on_delete=models.SET_NULL)
#     # topic = models.CharField(choices=TOPIC_CHOICES, null=True, max_length=100)
#     # q = models.CharField(blank=True, max_length=100)
#     # active = models.BooleanField(default=False)
#     # user = models.ForeignKey(
#     #     'auth.User', related_name='rss', on_delete=models.CASCADE)

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