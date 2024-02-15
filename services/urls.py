# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.ServiceListCreateAPIView.as_view(), name='service-list-create'),
    path('services/<int:pk>/', views.ServiceRetrieveUpdateDestroyAPIView.as_view(), name='service-retrieve-update-destroy'),
    path('patient-services/', views.PatientServiceListCreateAPIView.as_view(), name='patient-service-list-create'),
    path('patient-services/<int:pk>/', views.PatientServiceRetrieveUpdateDestroyAPIView.as_view(), name='patient-service-retrieve-update-destroy'),
]
