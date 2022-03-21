import email
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login

# import logging

# logger = logging.getLogger(__name__)


@api_view(['POST'])
def login(request):
    loginSerializer = LoginSerializer(data=request.data)
    if loginSerializer.is_valid():
        authUser = loginSerializer.login(
            loginSerializer.validated_data, request)
        if authUser is None:
            return Response('Invalid credentails', status=status.HTTP_401_UNAUTHORIZED)
        return Response(UserSerializer(authUser).data)

    return Response(loginSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
