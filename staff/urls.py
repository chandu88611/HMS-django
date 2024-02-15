from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.StaffListCreateAPIView.as_view(), name='staff-list-create'),
    path('staff/<int:pk>/', views.StaffRetrieveUpdateDestroyAPIView.as_view(), name='staff-detail'),
    path('staff/department/<str:department>/', views.StaffListByDepartmentAPIView.as_view(), name='staff-list-by-department'),
    path('staff/role/<str:role>/', views.StaffListByRoleAPIView.as_view(), name='staff-list-by-role'),
]
