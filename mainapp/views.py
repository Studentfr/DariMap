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
    drugs = models.Drug.objects.get(id=pk)
    serializer = DrugSerializer(drugs, many=False)
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
    return Response('Item deleted successfully')