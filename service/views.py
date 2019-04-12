from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from users.models import User, Doctor, Patient

from .models import Prescription,Hospital
from django.http import HttpResponse
from django.views.generic import View,ListView
from django.template.loader  import get_template
from .utils import render_to_pdf
from . import models

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

# Create your views here.

class CreatePrescription(LoginRequiredMixin, generic.CreateView):
    #form_class = forms.PostForm
    fields = ('patient','medicine_name', 'comment')
    model = models.Prescription
    template_name = "eprescription/prescription_form.html"
    success_url = reverse_lazy("patients")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.doctor_name = self.request.user
        self.object.save()
        return super().form_valid(form)


class HospitalListView(ListView):
    model = Hospital
    context_object_name = 'hospitals'



class UserPrescriptionList(LoginRequiredMixin, ListView):
    models = Prescription
    context_object_name = 'prescriptions'
    template_name = 'service/prescription_list.html'

    def get_queryset(self):
        user = get_object_or_404(User, id = self.kwargs.get('user_id'))
        return Prescription.objects.filter(doctor_name = user).order_by('-date_posted')

class GeneratePDF(View):
    def get(self,request,*args,**kwargs):
        template = get_template("eprescription/prescription.html")
        context = {
            'invoice_id':123,
            "customer_name":'nirob',
            "Amount": 52.5,
            "today" : "Today"
            }
        html = template.render(context)
        pdf = render_to_pdf('eprescription/prescription.html',context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("123456")
            content = "inline; filename='%s'" %(filename)
            response['content-Disposition'] = content
            return response
        return HttpResponse("Not Found")
