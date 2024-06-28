from django.shortcuts import render
from .models import DealerLocation, Car, Version, Feature
from .serializers import DealerLocationSerializer, CarSerializer, VersionSerializer, FeatureSerializer, UserSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .filters import CarFilter, VersionFilter, FeatureFilter
from django.contrib.auth.models import User
from rest_framework.response import Response

class DealerLocationViewSet(viewsets.ModelViewSet):
    queryset = DealerLocation.objects.all()
    serializer_class = DealerLocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['make', 'model', 'year']
    filterset_class = CarFilter

class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['car', 'name', 'price']
    filterset_class = VersionFilter
    
class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['name']
    filter_class = FeatureFilter

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        if not IsAdminUser().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)