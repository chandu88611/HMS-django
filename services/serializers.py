# serializers.py

from rest_framework import serializers
from .models import Service, PatientService

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class PatientServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientService
        fields = '__all__'
