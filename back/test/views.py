from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from . import serializers
from django.contrib.auth import authenticate, login as base_login
from pprint import pprint
# Create your views here.
# def test()

# @ensure_csrf_cookie
@api_view(['GET', 'POST'])
def test(request, format=None):
    return Response('test')

@api_view(['GET', 'POST'])
def test2(request, format=None):
    token = get_token(request=request);
    return Response(token)

@ensure_csrf_cookie
@api_view(['GET'])
def set_csrf_token(request):
    return Response('test')

@api_view(['POST'])
def login(request):
    user = User.objects.get(pk=1)
    base_login(request, user)
    return Response(serializers.UserSerializer(user).data)

@api_view(['GET'])
def me(request):
    user = request.user
    # base_login(request, user)
    return Response(serializers.UserSerializer(user).data)