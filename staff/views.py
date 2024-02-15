from rest_framework import generics
from .models import Staff
from .serializers import StaffSerializer

class StaffListCreateAPIView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffListByDepartmentAPIView(generics.ListAPIView):
    serializer_class = StaffSerializer

    def get_queryset(self):
        department = self.kwargs['department']
        return Staff.objects.filter(department=department)

class StaffListByRoleAPIView(generics.ListAPIView):
    serializer_class = StaffSerializer

    def get_queryset(self):
        role = self.kwargs['role']
        return Staff.objects.filter(role=role)
