from django.shortcuts import render
from rest_framework import viewsets
from .models import DealerLocation, Car, Version, Feature
from .serializers import DealerLocationSerializer, CarSerializer, VersionSerializer, FeatureSerializer

class DealerLocationViewSet(viewsets.ModelViewSet):
    queryset = DealerLocation.objects.all()
    serializer_class = DealerLocationSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer