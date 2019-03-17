from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from services.models import Eprescription
from services.forms import EprescriptionForm
# Create your views here.
# class eprescription(TemplateView):
#     template_name = 'eprescription/eprescription.html'
def eprescription(request):
    form = EprescriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EprescriptionForm()
    context = {
        'form':form
    }
    return render(request,"eprescription/eprescription.html",context)
