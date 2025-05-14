from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)


class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    clinic_address = models.TextField()
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"دکتر {self.user.get_full_name()}"


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    national_id = models.CharField(max_length=10)

    def __str__(self):
        return self.user.get_full_name()
