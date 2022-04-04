from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UpworkSerializer, SecretSerializer, JobListSerializer, JobMarkReadSerializer, JobMarkFavouriteSerializer, FilterUpworkSerializer, FilterCountrySerializer
from .models import Upwork, Secret, Job, Country
from .permissions import SecretGetSavePermission
from django.core import serializers
from django.db.models import Prefetch
from django.contrib.auth.models import User
from django_filters import rest_framework as filters


class UpworkViewSet(viewsets.ModelViewSet):
    queryset = Upwork.objects.all()
    serializer_class = UpworkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Upwork.objects.filter(user_id=self.request.user.id).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class JobListFilter(filters.FilterSet):
    only_unread = filters.BooleanFilter(method='only_unread_filter')
    only_favourited = filters.BooleanFilter(method='only_favourited_filter')

    class Meta:
        model = Job
        fields = ['rss_id', 'country_id']

    def only_unread_filter(self, queryset, name, value):
        if value == True:
            return queryset.exclude(readed_users__id=self.request.user.id)
        return queryset

    def only_favourited_filter(self, queryset, name, value):
        if value == True:
            return queryset.filter(favourited_users__id=self.request.user.id)
        return queryset


class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = JobListFilter

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
    permission_classes = [permissions.IsAuthenticated, SecretGetSavePermission]

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


class JobFilters(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        rsss = Upwork.objects.filter(user=request.user).order_by('type')
        countries = Country.objects.order_by('name')
        response = {
            'rsss': FilterUpworkSerializer(rsss, many=True).data,
            'countries': FilterCountrySerializer(countries, many=True).data,
        }
        return Response(response)
