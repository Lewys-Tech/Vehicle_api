from django.contrib import admin
from django.urls import path
from vehicle_api.views import vehicle_list, vehicle_create

urlpatterns = [
    path('', vehicle_create),
    path('list/', vehicle_list),
    path('<int:pk>/', vehicle_create),
]