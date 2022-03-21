from django.shortcuts import render
from rest_framework import viewsets, permissions

from .serializers import UpworkSerializer
from .models import Upwork
# Create your views here.


class UpworkViewSet(viewsets.ModelViewSet):
    queryset = Upwork.objects.all()
    serializer_class = UpworkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Upwork.objects.filter(user_id=self.request.user.id).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
