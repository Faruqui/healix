from django.db import models
from users.models import Patient, Doctor
from django.utils import timezone
# Create your models here.

class Eprescription(models.Model):
    pat = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
