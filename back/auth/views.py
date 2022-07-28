import email
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import LoginSerializer, UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import logout as base_logout
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

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
            return Response({'message': 'Invalid credentails'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(UserSerializer(authUser).data)

    return Response(loginSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register(request):
    registerSerializer = RegisterSerializer(data=request.data)
    registerSerializer.is_valid(raise_exception=True)
    newUser = registerSerializer.register(registerSerializer.validated_data, request)
    if newUser is None:
        return Response({'message': 'Somerthing went wrong'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(UserSerializer(newUser).data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    base_logout(request)

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def me(request):
    return Response(UserSerializer(request.user).data)
