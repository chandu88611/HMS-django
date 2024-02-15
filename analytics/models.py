# staff/models.py

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Staff(models.Model):
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('admin', 'Administrative Staff'),
    )

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        abstract = True

class Doctor(Staff):
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.name}, {self.specialization}"

class Nurse(Staff):
    shift = models.CharField(max_length=50)

    def __str__(self):
        return f"Nurse {self.name}"

class AdministrativeStaff(Staff):
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.position}"
