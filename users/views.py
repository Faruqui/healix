from django.shortcuts import render, redirect
from .forms import UserRegisterForm, DoctorUpdateForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Patient, Doctor
from django.views.generic import ListView, DetailView

# Create your views here.

def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            return redirect('login')
            #username = form.cleaned_data.get('username')
    else:
        u_form = UserRegisterForm()

    context = {
        'u_form' : u_form,
        'title' : 'Register',
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def editdocprofile(request):
    if request.method == 'POST':
        form = DoctorUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = DoctorUpdateForm(instance=request.user)

    context = {
        'title' : 'Edit Profile',
        'form' : form,
    }
    return render(request, 'users/editdocprofile.html', context)


class PatientListView(ListView):
    model = Patient
    context_object_name = 'patients'

class DoctorListView(ListView):
    model = Doctor
    context_object_name = 'doctors'
