import uuid
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User, Group
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


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True)

    def register(self, validated_data, request):
        try:
            userData = validated_data
            userData['username'] = 'user1'
            user = User.objects.create_user(
                uuid.uuid4(), userData.get('email'))
            user.set_password(userData.get('password'))
            user.save()
            user.groups.add(self.get_defaul_group())
            base_login(request, user)
            return user
        except:
            return None

    def get_defaul_group(self):
        group, created = Group.objects.get_or_create(name='user')
        return group


class UserSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'permissions']

    def get_permissions(self, user):
        return user.get_all_permissions()
