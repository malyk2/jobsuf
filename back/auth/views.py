import email
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import LoginSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import logout as base_logout

# import logging

# logger = logging.getLogger(__name__)


@ensure_csrf_cookie
@api_view(['GET'])
def csrf(request):
    return Response()


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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    base_logout(request)

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    return Response(UserSerializer(request.user).data)
