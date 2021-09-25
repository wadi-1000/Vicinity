from django.shortcuts import render,redirect
from .models import Neighbourhood
from .forms import UploadNewNeighbourhood
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
        form=UploadNewNeighbourhood(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood=form.save(commit=False)
            neighbourhood.user=current_user
            neighbourhood.save()

        return redirect('viewhood')

    else:
        form=UploadNewNeighbourhood()

    return render(request, 'uploadhood.html', {"form":form})

@login_required
def viewHood(request):
    
    hoods = Neighbourhood.objects.all()
    context = {
       
        'hoods':hoods
      }

    return render(request,'hood.html', context)

@login_required
def hood(request,pk):
    hood=Neighbourhood.objects.filter(id=pk)
    current_user=request.user


    return render(request, 'viewhood.html', {"hood":hood})


@login_required
def uploadBuisness(request):
    form=UploadNewBuisness()
    current_user=request.user

    if request.method =="POST":
        form=UploadNewBuisness(request.POST, request.FILES)
        if form.is_valid():
            buisness=form.save(commit=False)
            buisness.user=current_user
            buisness.save()

        return redirect('viewhood')

    else:
        form=UploadNewBuisness()

    return render(request, 'uploadbuisness.html', {"form":form})

    

