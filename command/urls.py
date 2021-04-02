from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('api/return-pin', views.return_pin),
    path('control-pin/', views.change_pin),
]