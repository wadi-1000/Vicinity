from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,  ProfileUpdateForm
from .models import Profile



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {"form":form})


