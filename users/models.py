from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_patient = models.BooleanField('patient status', default=False)
    is_doctor = models.BooleanField('doctor status', default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    health_problem = models.CharField(max_length = 200, default = 'nothing')
    height = models.FloatField(null = True)
    weight = models.FloatField(null = True)

    def __str__(self):
        return self.user.username

    def calculate_bmi(self):
        return round ( (self.weight/(self.height**2)), 3 )


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #patient = models.OneToManyField(Patient, on_delete=models.CASCADE)
    specialization = models.CharField(max_length = 200)

class Prescription(models.Model):
    
