# telemedicine/models.py

from django.db import models
from patients.models import Patient  # Import the Patient model from the patients app
from staff.models import Staff  # Import the Staff model from the staff app

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Staff, on_delete=models.CASCADE)
    prescription_date = models.DateField()
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient} by {self.doctor} on {self.prescription_date}"
