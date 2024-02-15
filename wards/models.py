# wards/models.py

from django.db import models

class Ward(models.Model):
    TYPE_CHOICES = (
        ('general', 'General'),
        ('private', 'Private'),
        ('intensive_care', 'Intensive Care'),
        ('other', 'Other'),
    )

    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
    )

    ward_number = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    capacity = models.IntegerField()
    occupancy = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Available')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ward {self.name} (Number: {self.ward_number})"
