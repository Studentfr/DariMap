from django.urls import path

from mainapp import views

urlpatterns = [
    path('', views.index),
    path('drug-list/', views.drugList),
]