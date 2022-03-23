from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UpworkSerializer, SecretSerializer
from .models import Upwork, Secret
from django.core import serializers


class UpworkViewSet(viewsets.ModelViewSet):
    queryset = Upwork.objects.all()
    serializer_class = UpworkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Upwork.objects.filter(user_id=self.request.user.id).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SecretGetSave(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        secret = self.get_secret(request)
        serializer = SecretSerializer(secret)
        return Response(serializer.data)

    def post(self, request, format=None):
        secret = self.get_secret(request)
        serializer = SecretSerializer(secret, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_secret(self, request):
        try:
            return request.user.rss_secret
        except Secret.DoesNotExist:
            return None
