from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics, filters, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from mainapp import models
from rest_framework.authtoken.models import Token


@api_view(['GET'])
def index(request):
    return Response("hello")


@api_view(['GET'])
def drugList(request):
    drugs = models.Drug.objects.all()
    serializer = DrugSerializer(drugs, many=True)
    return Response(serializer.data)


class drugListDetailFilter(generics.ListAPIView):
    queryset = models.Pharmacy_Drug.objects.all()
    serializer_class = Pharmacy_DrugSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$drug_id__name']
    def get_queryset(self):
        slug = self.request.query_params.get('pharmacy_id', None)
        return Pharmacy_Drug.objects.filter(pharmacy_id=slug)



@api_view(['GET'])
def drugDetail(request, pk):
    drug = models.Drug.objects.get(id=pk)
    serializer = DrugSerializer(drug, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def drugCreate(request):
    new_drug = request.data
    try:
        check = models.Drug.objects.get(name=new_drug['name'])
        serializer = DrugSerializer(instance=check, data=new_drug)
        if serializer.is_valid():
            serializer.save()
    except:
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
    serializer = PharmacyCreationSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print(request.data, 'valid')
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
def phDrugListId(request, pk):
    phDrugs = models.Pharmacy_Drug.objects.filter(pharmacy_id=pk)
    serializer = Pharmacy_DrugSerializer(phDrugs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def phDrugDetail(request, pk):
    phDrug = models.Pharmacy_Drug.objects.get(id=pk)
    serializer = Pharmacy_DrugSerializer(phDrug, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def phDrugCreate(request):
    new_drug = request.data
    try:
        check = models.Pharmacy_Drug.objects.get(drug_id=new_drug['drug_id'], pharmacy_id=new_drug['pharmacy_id'])
        serializer = Pharmacy_DrugCreationSerializer(instance=check, data=new_drug)
        if serializer.is_valid():
            serializer.save()
    except:
        serializer = Pharmacy_DrugCreationSerializer(data=new_drug)
        print(new_drug)
        if serializer.is_valid():
            print(new_drug, ' Valid')
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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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


@api_view(['GET'])
def coordinateList(request):
    coordinates = models.Coordinate.objects.all()
    serializer = CoordinateSerializer(coordinates, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def coordinateDetail(request, pk):
    coordinate = models.Coordinate.objects.get(id=pk)
    serializer = CoordinateSerializer(coordinate, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def coordinateCreate(request):
    serializer = CoordinateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def coordinateUpdate(request, pk):
    coordinate = models.Coordinate.objects.get(id=pk)
    serializer = CoordinateSerializer(instance=coordinate, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def coordinateDelete(request, pk):
    coordinate = models.Coordinate.objects.get(id=pk)
    coordinate.delete()
    return Response('Coordinate has been deleted successfully')


@api_view(['GET'])
def transactionList(request):
    transactions = models.Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def transactionDetail(request, pk):
    transaction = models.Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(transaction, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def transactionCreate(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def transactionUpdate(request, pk):
    transaction = models.Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(instance=transaction, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def transactionDelete(request, pk):
    transaction = models.Transaction.objects.get(id=pk)
    transaction.delete()
    return Response('Transaction has been deleted successfully')


@api_view(['GET'])
def fvPharmacyList(request):
    fvPharmacies = models.Favourite_Pharmacy.objects.all()
    serializer = FavouritePharmacySerializer(fvPharmacies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def fvPharmacyDetail(request, pk):
    fvPharmacy = models.Favourite_Pharmacy.objects.get(id=pk)
    serializer = FavouritePharmacySerializer(fvPharmacy, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def fvPharmacyCreate(request):
    serializer = FavouritePharmacySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def fvPharmacyUpdate(request, pk):
    fvPharmacy = models.Favourite_Pharmacy.objects.get(id=pk)
    serializer = FavouritePharmacySerializer(instance=fvPharmacy, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def fvPharmacyDelete(request, pk):
    fvPharmacy = models.Favourite_Pharmacy.objects.get(id=pk)
    fvPharmacy.delete()
    return Response('Favourite pharmacy has been deleted successfully')

@api_view(['GET'])
def get_user(request):
    slug = request.query_params.get('token', None)
    u = Token.objects.get(key=slug)
    print(u.user.id)
    return HttpResponse(u.user.id)