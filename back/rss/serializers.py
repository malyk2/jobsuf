from rest_framework import serializers
from .models import Upwork, Secret, Job, Country


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

    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'content',
            'upwork_id',
            'rate_from',
            'rate_to',
            'published',
            'created',
            'country',
            'rss',
            'skills',
        ]
