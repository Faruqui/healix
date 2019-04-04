from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Doctor

CHOICES=[('item1','item 1'),
         ('item2','item 2')]

class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()
    email = forms.EmailField(label = (u'Email Adress')) #for labelling

    class Meta:
        model = User
        fields = ['username', 'email', 'is_doctor' ,'is_patient' ,'password1', 'password2']


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialization', 'education', 'image']
