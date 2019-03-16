from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
# Create your views here.
class eprescription(TemplateView):
    template_name = 'eprescription/eprescription.html'
