from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UpworkSerializer, SecretSerializer, JobListSerializer, JobMarkReadSerializer, JobMarkFavouriteSerializer, FilterUpworkSerializer, FilterCountrySerializer
from .models import Upwork, Secret, Job, Country, JobFavouritedUsers
from .permissions import SecretGetSavePermission
from django.core import serializers
from django.db.models import Prefetch, Q
from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from dateutil.relativedelta import relativedelta
from datetime import datetime

class UpworkViewSet(viewsets.ModelViewSet):
    queryset = Upwork.objects.all()
    serializer_class = UpworkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Upwork.objects.filter(user_id=self.request.user.id).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class JobListFilter(filters.FilterSet):
    budget__gte = filters.NumberFilter(field_name='budget', lookup_expr='gte')
    budget__lte = filters.NumberFilter(field_name='budget', lookup_expr='lte')
    rate_from__gte = filters.NumberFilter(field_name='rate_from', lookup_expr='gte')
    rate_from__lte = filters.NumberFilter(field_name='rate_from', lookup_expr='lte')
    rate_to__gte = filters.NumberFilter(field_name='rate_to', lookup_expr='gte')
    rate_to__lte = filters.NumberFilter(field_name='rate_to', lookup_expr='lte')
    created = filters.DateFilter(field_name='created', lookup_expr='date')
    created__gte = filters.DateFilter(field_name='created', lookup_expr='date__gte')
    created__lte = filters.DateFilter(field_name='created', lookup_expr='date__lte')
    published = filters.DateFilter(field_name='published', lookup_expr='date')
    published__gte = filters.DateFilter(field_name='published', lookup_expr='date__gte')
    published__lte = filters.DateFilter(field_name='published', lookup_expr='date__lte')
    search = filters.CharFilter(field_name='search_vector')
    only_unread = filters.BooleanFilter(method='only_unread_filter')
    only_favourited = filters.BooleanFilter(method='only_favourited_filter')
    favourited_rate = filters.NumberFilter(method='favourited_rate_filter')
    no_rate = filters.BooleanFilter(method='no_rate_filter')
    period = filters.CharFilter(method='period_filter')

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
    
    def favourited_rate_filter(self, queryset, name, value):
        if value != None:
            return queryset.filter(pivot_favourited_users__rate=value)
        return queryset
    
    def no_rate_filter(self, queryset, name, value):
        if value:
            return queryset.filter(rate_to__isnull=True, rate_from__isnull=True, budget__isnull=True)
        return queryset

    def period_filter(self, queryset, name, value):
        if value != None:
            delta = None
            if value == 'last_week':
                delta = relativedelta(weeks=1);
            if value == 'last_2_weeks':
                delta = relativedelta(weeks=2);
            if value == 'last_month':
                delta = relativedelta(months=1);
            if value == 'last_2_months':
                delta = relativedelta(months=2);
            if delta:
                return queryset.filter(created__date__gte=(datetime.now() - delta))
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
            Prefetch('pivot_favourited_users', queryset=JobFavouritedUsers.objects.filter(user_id=self.request.user.id), to_attr='pivot_favourited_auth_data'),
        ).filter((Q(rss__user_id=self.request.user.id)|Q(rss__public=True))).order_by('-created').all()


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
                pivot_data = rate and {'rate': rate} or None
                JobFavouritedUsers.objects.update_or_create(user_id=me.id, job_id=item.get('id'), defaults=pivot_data)
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
        rsss = Upwork.objects.filter((Q(user=request.user)|Q(public=True))).order_by('type')
        countries = Country.objects.filter().order_by('name')
        response = {
            'rsss': FilterUpworkSerializer(rsss, many=True).data,
            'countries': FilterCountrySerializer(countries, many=True).data,
        }
        return Response(response)
