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

    path('pharmacy-drug-list/', views.phDrugList, name="pharmacy-drug-list"),
    path('pharmacy-drug-create/', views.phDrugCreate, name="pharmacy-drug-create"),
    path('pharmacy-drug-detail/<int:pk>/', views.phDrugDetail, name="pharmacy-drug-detail"),
    path('pharmacy-drug-update/<int:pk>/', views.phDrugUpdate, name="pharmacy-drug-update"),
    path('pharmacy-drug-delete/<int:pk>/', views.phDrugDelete, name="pharmacy-drug-delete"),

    path('user-list/', views.userList, name="user-list"),
    path('user-detail/<int:pk>/', views.userDetail, name="user-detail"),
    path('user-update/<int:pk>/', views.userUpdate, name="user-update"),
    path('user-delete/<int:pk>/', views.userDelete, name="user-delete"),
    path('user-create/', views.userCreate, name="user-create"),

    path('coordinate-list/', views.coordinateList, name="coordinate-list"),
    path('coordinate-detail/<int:pk>/', views.coordinateDetail, name="coordinate-detail"),
    path('coordinate-update/<int:pk>/', views.coordinateUpdate, name="coordinate-update"),
    path('coordinate-delete/<int:pk>/', views.coordinateDelete, name="coordinate-delete"),
    path('coordinate-create/', views.coordinateCreate, name="coordinate-create"),

]