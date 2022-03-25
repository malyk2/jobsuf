from pytz import timezone
from rest_framework import serializers
from .models import Upwork, Secret, Job, Country
from django.conf import settings


class UpworkSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField()
    # highlight = serializers.HyperlinkedIdentityField(
    #     view_name='snippet-highlight', format='html')

    class Meta:
        model = Upwork
        fields = [
            'id',
            'title',
            'type',
            'topic',
            'q',
            'active',
            'user_id',
            'created',
            # 'user',
        ]


class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = [
            'org_uid',
            'security_token',
            'user_uid',
        ]


class JobListSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name',
    )
    rss = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title',
    )
    skills = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )
    is_readed_by_auth_user = serializers.SerializerMethodField()
    is_favourited = serializers.SerializerMethodField()
    created = serializers.DateTimeField(
        default_timezone=timezone(settings.FRONT_TIME_ZONE))

    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'content',
            'upwork_id',
            'rate_from',
            'rate_to',
            'budget',
            'published',
            'created',
            'country',
            'rss',
            'skills',
            'is_readed_by_auth_user',
            'is_favourited',
        ]

    def get_is_readed_by_auth_user(self, job):
        return bool(job.readed_auth_user)  # from view's Prefetch
    def get_is_favourited(self, job):
        return bool(job.favourited_auth_user)  # from view's Prefetch


class JobMarkReadSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    readed = serializers.BooleanField()

class JobMarkFavouriteSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    favourited = serializers.BooleanField()
    rate = serializers.IntegerField(min_value=0, max_value=5, required=False)
