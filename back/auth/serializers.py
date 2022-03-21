import email
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import login as base_login


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(required=True)

    def login(self, validated_data, request):
        try:
            user = User.objects.get(email=validated_data.get('email'))
        except User.DoesNotExist:
            return None
        if user.check_password(validated_data.get('password')):
            base_login(request, user)
            return user
        return None


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
