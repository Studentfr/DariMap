from django.urls import path

from mainapp import views

urlpatterns = [
    path('', views.index),

    path('drug-list/', views.drugList, name="drug-list"),
    path('drug-detail/<int:pk>/', views.drugDetail, name="drug-detail"),
    path('drug-update/<int:pk>/', views.drugUpdate, name="drug-update"),
    path('drug-delete/<int:pk>/', views.drugDelete, name="drug-delete"),
    path('drug-create/', views.drugCreate, name="drug-create"),

    path('pharmacy-list/', views.pharmacyList, name="pharmacy-list"),
    path('pharmacy-detail/<int:pk>/', views.pharmacyDetail, name="pharmacy-detail"),
    path('pharmacy-update/<int:pk>/', views.pharmacyUpdate, name="pharmacy-update"),
    path('pharmacy-delete/<int:pk>/', views.pharmacyDelete, name="pharmacy-delete"),
    path('pharmacy-create/', views.pharmacyCreate, name="pharmacy-create"),
]