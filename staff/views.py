from rest_framework import generics
from rest_framework.response import Response
from .models import Staff
from .serializers import StaffSerializer

class StaffListCreateAPIView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'Staff list retrieved successfully',
            'data': serializer.data
        }
        return Response(data)

class StaffRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = {
            'status': 'success',
            'message': 'Staff details retrieved successfully',
            'data': serializer.data
        }
        return Response(data)

class StaffListByDepartmentAPIView(generics.ListAPIView):
    serializer_class = StaffSerializer

    def get_queryset(self):
        department = self.kwargs['department']
        return Staff.objects.filter(department=department)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'Staff list retrieved successfully',
            'data': serializer.data
        }
        return Response(data)

class StaffListByRoleAPIView(generics.ListAPIView):
    serializer_class = StaffSerializer

    def get_queryset(self):
        role = self.kwargs['role']
        return Staff.objects.filter(role=role)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'Staff list retrieved successfully',
            'data': serializer.data
        }
        return Response(data)
