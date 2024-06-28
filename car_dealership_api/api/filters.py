from django_filters import rest_framework as filters
from .models import Car, Version, Feature

class CarFilter(filters.FilterSet):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year']

class VersionFilter(filters.FilterSet):
    class Meta:
        model = Version
        fields = ['car', 'name', 'price']

class FeatureFilter(filters.FilterSet):
    class Meta:
        model = Feature
        fields = ['name']