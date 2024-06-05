from rest_framework import serializers
from .models import DealerLocation, Car, Version, Feature

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name', 'description', 'version']

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ['id', 'name', 'price', 'car', 'description']

class CarSerializer(serializers.ModelSerializer):
    Versions = VersionSerializer(many=True, read_only=True)
    Features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'description', 'image', 'Versions', 'Features']


class DealerLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerLocation
        fields =['id', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number', 'email', 'website']