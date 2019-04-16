from django.contrib import admin
from service.models import Prescription,Hospital,Location
# Register your models here.
admin.site.register(Prescription)
admin.site.register(Hospital)
admin.site.register(Location)
