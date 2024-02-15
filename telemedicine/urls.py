from django.urls import path
from .views import PrescriptionListCreateAPIView, PrescriptionRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('prescriptions/', PrescriptionListCreateAPIView.as_view(), name='prescription-list-create'),
    path('prescriptions/<int:pk>/', PrescriptionRetrieveUpdateDestroyAPIView.as_view(), name='prescription-detail'),
]
