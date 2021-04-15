from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from mainapp import models


@api_view(['GET'])
def index(request):
    return Response("hello")


@api_view(['GET'])
def drugList(request):
    drugs = models.Drug.objects.all()
    serializer = DrugSerializer(drugs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def drugDetail(request, pk):
    drug = models.Drug.objects.get(id=pk)
    serializer = DrugSerializer(drug, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def drugCreate(request):
    serializer = DrugSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def drugUpdate(request, pk):
    drug = models.Drug.objects.get(id=pk)
    serializer = DrugSerializer(instance=drug, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def drugDelete(request, pk):
    drug = models.Drug.objects.get(id=pk)
    drug.delete()
    return Response('Drug has deleted successfully')


# Pharmacy vies
@api_view(['GET'])
def pharmacyList(request):
    pharmacies = models.Pharmacy.objects.all()
    serializer = PharmacySerializer(pharmacies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def pharmacyDetail(request, pk):
    pharmacy = models.Pharmacy.objects.get(id=pk)
    serializer = PharmacySerializer(pharmacy, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def pharmacyCreate(request):
    serializer = PharmacySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def pharmacyUpdate(request, pk):
    pharmacy = models.Pharmacy.objects.get(id=pk)
    serializer = PharmacySerializer(instance=pharmacy, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def pharmacyDelete(request, pk):
    pharmacy = models.Pharmacy.objects.get(id=pk)
    pharmacy.delete()
    return Response('Pharmacy has been deleted successfully')


@api_view(['GET'])
def phDrugList(request):
    phDrugs = models.Pharmacy_Drug.objects.all()
    serializer = Pharmacy_DrugSerializer(phDrugs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def phDrugDetail(request, pk):
    phDrug = models.Pharmacy_Drug.objects.get(id=pk)
    serializer = Pharmacy_DrugSerializer(phDrug, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def phDrugCreate(request):
    serializer = Pharmacy_DrugSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def phDrugUpdate(request, pk):
    phDrug = models.Pharmacy_Drug.objects.get(id=pk)
    serializer = Pharmacy_DrugSerializer(instance=phDrug, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def phDrugDelete(request, pk):
    phDrug = models.Pharmacy_Drug.objects.get(id=pk)
    phDrug.delete()
    return Response('Drug in the Pharmacy has been deleted successfully')


@api_view(['GET'])
def userList(request):
    users = models.User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def userDetail(request, pk):
    user = models.User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def userUpdate(request, pk):
    user = models.User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def userDelete(request, pk):
    user = models.User.objects.get(id=pk)
    user.delete()
    return Response('User has been deleted successfully')


@api_view(['GET'])
def fvDrugList(request):
    fvDrugs = models.Favourite_Drug.objects.all()
    serializer = Favourite_DrugSerializer(instance=fvDrugs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def fvDrugDetail(request, pk):
    fvDrug = models.Favourite_Drug.objects.get(id=pk)
    serializer = Favourite_DrugSerializer(fvDrug, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def fvDrugCreate(request):
    serializer = Favourite_DrugSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def fvDrugUpdate(request, pk):
    fvDrug = models.Favourite_Drug.objects.get(id=pk)
    serializer = Favourite_DrugSerializer(instance=fvDrug, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def fvDrugDelete(request, pk):
    fvDrug = models.Favourite_Drug.objects.get(id=pk)
    fvDrug.delete()
    return Response('Favourite Drug has been deleted successfully')
