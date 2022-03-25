from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UpworkSerializer, SecretSerializer, JobListSerializer, JobMarkReadSerializer, JobMarkFavouriteSerializer
from .models import Upwork, Secret, Job
from django.core import serializers
from django.db.models import Prefetch
from django.contrib.auth.models import User


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
        return Job.objects.prefetch_related(
            'country',
            'rss',
            'skills',
            Prefetch('readed_users', User.objects.filter(
                id=self.request.user.id), 'readed_auth_user'),
            Prefetch('favourited_users', User.objects.filter(
                id=self.request.user.id), 'favourited_auth_user'),
        ).filter(rss__user_id=self.request.user.id).order_by('-created').all()


class JobMarkRead(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, format=None):
        serializer = JobMarkReadSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        me = request.user
        for item in serializer.validated_data:
            id = item.get('id')
            if item.get('readed'):
                me.readed_rss_jobs.add(id)
            else:
                me.readed_rss_jobs.remove(id)

        return Response(status=status.HTTP_204_NO_CONTENT)


class JobMarkFavourite(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, format=None):
        serializer = JobMarkFavouriteSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        me = request.user
        for item in serializer.validated_data:
            if item.get('favourited'):
                rate = item.get('rate')
                through_defaults = rate and {'rate': rate} or None
                me.favourited_rss_jobs.add(
                    item.get('id'), through_defaults=through_defaults)
            else:
                me.favourited_rss_jobs.remove(item.get('id'))

        return Response(status=status.HTTP_204_NO_CONTENT)


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
