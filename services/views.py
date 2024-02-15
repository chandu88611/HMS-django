# views.py

from rest_framework import generics
from .models import Service, PatientService
from .serializers import ServiceSerializer, PatientServiceSerializer

class ServiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class PatientServiceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PatientServiceSerializer

    def get_queryset(self):
 
        return PatientService.objects.filter(patient__discharge_date__isnull=True)

class PatientServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientService.objects.all()
    serializer_class = PatientServiceSerializer
