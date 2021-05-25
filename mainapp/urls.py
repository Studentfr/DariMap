from django.urls import path, include

from mainapp import views
from rest_framework import routers

from mainapp.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('get-user/', views.get_user, name="get-user"),

    path('drug-list/', views.drugList, name="drug-list"),
    path('drug-detail/<str:pk>/', views.drugDetail, name="drug-detail"),
    path('drug-search/custom/', views.drugListDetailFilter.as_view(), name="drug-search"),
    path('drug-create/', views.drugCreate, name="drug-create"),
    path('drug-update/<int:pk>/', views.drugUpdate, name="drug-update"),
    path('drug-delete/<int:pk>/', views.drugDelete, name="drug-delete"),

    path('pharmacy-list/', views.pharmacyList, name="pharmacy-list"),
    path('pharmacy-detail/<int:pk>/', views.pharmacyDetail, name="pharmacy-detail"),
    path('pharmacy-create/', views.pharmacyCreate, name="pharmacy-create"),
    path('pharmacy-update/<int:pk>/', views.pharmacyUpdate, name="pharmacy-update"),
    path('pharmacy-delete/<int:pk>/', views.pharmacyDelete, name="pharmacy-delete"),


    path('pharmacy-drug-list/', views.phDrugList, name="pharmacy-drug-list"),
    path('pharmacy-drug-list/<int:pk>', views.phDrugListId, name="pharmacy-drug-list"),
    path('pharmacy-drug-detail/<int:pk>/', views.phDrugDetail, name="pharmacy-drug-detail"),
    path('pharmacy-drug-create/', views.phDrugCreate, name="pharmacy-drug-create"),
    path('pharmacy-drug-update/<int:pk>/', views.phDrugUpdate, name="pharmacy-drug-update"),
    path('pharmacy-drug-delete/<int:pk>/', views.phDrugDelete, name="pharmacy-drug-delete"),

    path('user-list/', views.userList, name="user-list"),
    path('user-detail/<int:pk>/', views.userDetail, name="user-detail"),
    path('user-create/', views.userCreate, name="user-create"),
    path('user-update/<int:pk>/', views.userUpdate, name="user-update"),
    path('user-delete/<int:pk>/', views.userDelete, name="user-delete"),

    path('favourite-drug-list/<int:pk>', views.fvDrugList, name="favourite-drug-list"),
    path('favourite-drug-detail/<int:pk>/', views.fvDrugDetail, name="favourite-drug-detail"),
    path('favourite-drug-create/', views.fvDrugCreate, name="favourite-drug-create"),
    path('favourite-drug-update/<int:pk>/', views.fvDrugUpdate, name="favourite-drug-update"),
    path('favourite-drug-delete/<int:pk>/', views.fvDrugDelete, name="favourite-drug-delete"),

    path('transaction-list/', views.transactionList, name="transaction-list"),
    path('transaction-detail/<int:pk>/', views.transactionDetail, name="transaction-detail"),
    path('transaction-create/', views.transactionCreate, name="transaction-create"),
    path('transaction-update/<int:pk>/', views.transactionUpdate, name="transaction-update"),
    path('transaction-delete/<int:pk>/', views.transactionDelete, name="transaction-delete"),

    path('coordinate-list/', views.coordinateList, name="coordinate-list"),
    path('coordinate-detail/<int:pk>/', views.coordinateDetail, name="coordinate-detail"),
    path('coordinate-update/<int:pk>/', views.coordinateUpdate, name="coordinate-update"),
    path('coordinate-delete/<int:pk>/', views.coordinateDelete, name="coordinate-delete"),
    path('coordinate-create/', views.coordinateCreate, name="coordinate-create"),

    path('favourite-pharmacy-list/<int:pk>', views.fvPharmacyList, name="favourite-pharmacy-list"),
    path('favourite-pharmacy-detail/<int:pk>/', views.fvPharmacyDetail, name="favourite-pharmacy-detail"),
    path('favourite-pharmacy-update/<int:pk>/', views.fvPharmacyUpdate, name="favourite-pharmacy-update"),
    path('favourite-pharmacy-delete/<int:pk>/', views.fvPharmacyDelete, name="favourite-pharmacy-delete"),
    path('favourite-pharmacy-create/', views.fvPharmacyCreate, name="favourite-pharmacy-create"),


]