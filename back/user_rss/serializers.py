from rest_framework import serializers
from .models import Upwork

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