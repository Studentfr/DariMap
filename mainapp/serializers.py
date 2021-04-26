from rest_framework import serializers
from .models import *


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ['latitude', 'longitude']


class PharmacySerializer(serializers.ModelSerializer):
    coordinate_id = CoordinateSerializer()

    class Meta:
        model = Pharmacy
        fields = ['id', 'name', 'coordinate_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Pharmacy_DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy_Drug
        fields = '__all__'


class Favourite_DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite_Drug
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class FavouritePharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite_Pharmacy
        fields = '__all__'

