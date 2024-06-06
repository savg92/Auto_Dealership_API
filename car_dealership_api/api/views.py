from django.shortcuts import render
from .models import DealerLocation, Car, Version, Feature
from .serializers import DealerLocationSerializer, CarSerializer, VersionSerializer, FeatureSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class DealerLocationViewSet(viewsets.ModelViewSet):
    queryset = DealerLocation.objects.all()
    serializer_class = DealerLocationSerializer

# class CarViewSet(viewsets.ModelViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer



class DealerLocationViewSet(viewsets.ModelViewSet):
    queryset = DealerLocation.objects.all()
    serializer_class = DealerLocationSerializer
    permission_classes = [IsAuthenticated]  # Require authentication for all actions

# class CarViewSet(viewsets.ModelViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     # permission_classes = [IsAuthenticated, IsAdminUser]  # Require authentication and admin status
#     permission_classes = [IsAuthenticated]  # Require authentication and admin status

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            # No permissions are required for GET requests
            return []
        else:
            # For non-GET requests, req            # For non-GET requests, require authentication
            return [IsAuthenticated()]