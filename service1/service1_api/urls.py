
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('get_data', GetDataAPIView.as_view()),
    path('get_data/<str:pk>', GetDataDetailedAPIView.as_view())
]
