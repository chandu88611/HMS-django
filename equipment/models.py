# equipment/models.py

from django.db import models
from wards.models import Ward  # Import the Ward model from the wards app

class Equipment(models.Model):
    TYPE_CHOICES = (
        ('medical', 'Medical'),
        ('surgical', 'Surgical'),
        ('diagnostic', 'Diagnostic'),
        ('other', 'Other'),
    )

    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('In Use', 'In Use'),
        ('Under Maintenance', 'Under Maintenance'),
        ('Out of Service', 'Out of Service'),
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    location = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Available')
    last_maintenance = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
