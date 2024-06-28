from rest_framework import serializers
from .models import DealerLocation, Car, Version, Feature
from django.contrib.auth.models import User

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance