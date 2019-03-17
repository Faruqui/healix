from django import forms
from services.models import Eprescription
class EprescriptionForm(forms.ModelForm):
    class Meta():
        model = Eprescription
        fields='__all__'
