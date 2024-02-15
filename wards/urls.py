from django.urls import path
from .views import WardListCreateAPIView, WardRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('wards/', WardListCreateAPIView.as_view(), name='ward-list-create'),
    path('wards/<int:pk>/', WardRetrieveUpdateDestroyAPIView.as_view(), name='ward-detail'),
]
