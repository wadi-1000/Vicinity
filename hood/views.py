from django.shortcuts import render
from models import Neighbourhood
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def uploadNeighbourhood(request):
    form=UploadNewNeighbourhood()
    current_user=request.user

    if request.method =="POST":
        form=UploadNewProject(request.POST, request.FILES)
        if form.is_valid():
            hood=form.save(commit=False)
            hood.user=current_user
            hood.save()

        return redirect('home')

    else:
        form=UploadNewNeighbourhood()

    return render(request, 'uploadhood.html', {"form":form})