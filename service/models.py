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

class Location(models.Model):
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.address

    class Admin:
        list_display = ('city', 'country')

class Hospital(models.Model):
    name = models.CharField(max_length=160)
    phone = models.CharField(max_length=20)
    location = models.OneToOneField(Location,on_delete=models.CASCADE,null = True)


    def __str__(self):
        return self.name
    def __str__(self):
        return self.name

    class Admin:
        list_display = (
            'name',
            'phone',
            'location'
        )

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="doctors",on_delete=models.CASCADE)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="patients",on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    startTime = models.TimeField()
    endTime = models.TimeField()
    date = models.DateField()
def __str__(self):
    return self.doctor
