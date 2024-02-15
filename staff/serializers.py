from rest_framework import serializers
from .models import Staff

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'name', 'role', 'department', 'email', 'phone_number', 'address', 'assigned_patients', 'created_at']
