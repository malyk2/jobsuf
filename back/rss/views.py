from rest_framework import viewsets, permissions, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UpworkSerializer, SecretSerializer, JobListSerializer
from .models import Upwork, Secret, Job
from django.core import serializers


class UpworkViewSet(viewsets.ModelViewSet):
    queryset = Upwork.objects.all()
    serializer_class = UpworkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Upwork.objects.filter(user_id=self.request.user.id).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Job.objects.prefetch_related('country', 'rss', 'skills').filter(rss__user_id=self.request.user.id).order_by('-created').all()


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
        serializer.save(user=request.user)
        return Response(serializer.data)

    def get_secret(self, request):
        try:
            return request.user.rss_secret
        except Secret.DoesNotExist:
            return None
