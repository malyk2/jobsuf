from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.
# def test()

# @ensure_csrf_cookie
@api_view(['GET', 'POST'])
def test(request, format=None):
    token = get_token(request=request);
    return Response(token)

@api_view(['GET', 'POST'])
def test2(request, format=None):
    token = get_token(request=request);
    return Response(token)

@ensure_csrf_cookie
@api_view(['GET'])
def set_csrf_token(request):
    return Response('test')