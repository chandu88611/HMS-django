# billing/models.py

from django.db import models
from patients.models import Patient  # Import the Patient model from the patients app
from staff.models import Staff  # Import the Staff model from the staff app
from services.models import Service  # Import the Service model from the services app

class Billing(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('partial', 'Partial'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    staff_doctor = models.ForeignKey(Staff, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Billing for {self.patient} by {self.staff_doctor} (ID: {self.id})"
