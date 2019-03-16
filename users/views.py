from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

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
