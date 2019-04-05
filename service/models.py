from django.db import models
from django.utils import timezone
from users.models import Patient,Doctor
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class eprescriptions(models.Model):
    doctor_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Patient_name = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        null=True
    )
    medicine_name = models.TextField()
    comment = models.CharField(max_length=250,null=True)
    test = models.CharField(max_length=250,null=True)
    date_posted = models.DateTimeField(default=timezone.now)
