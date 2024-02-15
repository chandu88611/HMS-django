from django.db import models

class Staff(models.Model):
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('administrative', 'Administrative Staff'),
        ('other', 'Other'),
    )

    AVAILABILITY_CHOICES = (
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('on_leave', 'On Leave'),
    )
    
    name = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    department = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    availability_status = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    assigned_patients = models.ManyToManyField('patients.Patient', blank=True, related_name='assigned_staff')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role}: {self.user.username}"

class AttendanceLog(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Attendance log for {self.staff.name}"

