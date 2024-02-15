from django.urls import path
from .views import BillingListCreateAPIView, BillingRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('billings/', BillingListCreateAPIView.as_view(), name='billing-list-create'),
    path('billings/<int:pk>/', BillingRetrieveUpdateDestroyAPIView.as_view(), name='billing-detail'),
]
