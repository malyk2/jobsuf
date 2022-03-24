from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from . import serializers
from django.contrib.auth import authenticate, login as base_login
from pprint import pprint

from rss.models import Job,Country
# Create your views here.
# def test()
import json
from django.forms.models import model_to_dict

# @ensure_csrf_cookie
@api_view(['GET', 'POST'])
def test(request, format=None):
    
    job = Job.objects.get(pk='fc4dd68a-fbae-4934-915b-fd728f3afc36')
    print(job.skills)

    # country = Country.objects.create()
    # country = Country.objects.filter(name='Test contry').last()
    # job = Job.objects.create(country=country)
    # job = Job.objects.get(pk='fb953407-1622-4759-8095-f43fee09caf9')

    # data = {
    #     'title': 'test title',
    # }
    # job = Job.objects.create(**data);
    # country = job.country.create()
    # print(job.__dict__)
    # print(json.dumps(job))

    # return Response(job.created)
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