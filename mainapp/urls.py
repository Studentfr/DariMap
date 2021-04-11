from django.urls import path

from mainapp import views

urlpatterns = [
    path('', views.index),
    path('drug-list/', views.drugList, name="drug-list"),
    path('drug-detail/<int:pk>/', views.drugDetail, name="drug-detail"),
    path('drug-update/<int:pk>/', views.drugUpdate, name="drug-update"),
    path('drug-delete/<int:pk>/', views.drugDelete, name="drug-delete"),
    path('drug-create/', views.drugCreate, name="drug-create"),


]