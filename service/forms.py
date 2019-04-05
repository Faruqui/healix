from django import forms
#from users import User
from .models import eprescriptions

class EpresForm(forms.ModelForm):
    class Meta():
        model = eprescriptions
        fields = ['doctor_name','Patient_name','medicine_name','comment','test']
