# wards/views.py
from rest_framework import generics
from .models import Ward
from .serializers import WardSerializer

class WardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer

class WardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
