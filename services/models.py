from django.db import models
from django.db import connection
from django.contrib.auth.models import AbstractUser
from users.models import User
# Create your models here.
class Eprescription(models.Model):

    drug_name = models.CharField(max_length=120,null = True)
    days = models.IntegerField(null = True)
    comment = models.TextField(null = True)
    after_breakfirst = models.BooleanField()
    after_lunch = models.BooleanField()
    after_dinner = models.BooleanField()
    before_breakfrist = models.BooleanField()
    before_lunch = models.BooleanField()
    before_dinner = models.BooleanField()
