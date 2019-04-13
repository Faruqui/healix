from django.db import models
from django.utils import timezone
from users.models import Patient,Doctor
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Prescription(models.Model):
    doctor_name = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="eprescription", on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,null=True,related_name="eprescription", blank=True,on_delete=models.CASCADE)
    medicine_name = models.TextField()
    comment = models.CharField(max_length=250,null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('prescription-detail', kwargs={'pk': self.pk})



class Hospital(models.Model):
    name = models.CharField(max_length=160)
    area = models.CharField(null=True, max_length=200)
    address = models.CharField(null=True, max_length=200)
    phone = models.IntegerField(null=True)


    def __str__(self):
        return self.name
