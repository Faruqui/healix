from django.shortcuts import render
from .forms import EpresForm
from .models import eprescriptions
# Create your views here.
def eprescription(request):
    form = EpresForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=EpresForm()
    context={
        'form':form
    }
    return render(request,"eprescription/eprescription.html",context)
