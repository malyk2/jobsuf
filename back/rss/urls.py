from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UpworkViewSet

from django.contrib.auth import views as auth_views  # import this

# urlpatterns = [
#     path('login', views.login),
#     path('csrf', views.csrf),
#     path('me', views.me),
# ]

router = DefaultRouter()
router.register(r'upwork', views.UpworkViewSet)
# print(router.urls)
urlpatterns = [
    path('', include(router.urls)),
    path('secret/', views.SecretGetSave.as_view()),
    path('jobs/', views.JobList.as_view()),
    path('jobs/filter/', views.JobFilters.as_view()),
    path('jobs/read/', views.JobMarkRead.as_view()),
    path('jobs/favourite/', views.JobMarkFavourite.as_view()),

]
