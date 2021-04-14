from rest_framework import serializers
from .models import *


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'

class Pharmacy_DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy_Drug
        fields = '__all__'