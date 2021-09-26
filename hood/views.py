from django.shortcuts import render,redirect
from .models import Neighbourhood,Buisness
from .forms import UploadNewNeighbourhood,UploadNewBuisness
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



@login_required
def viewBizna(request):
    
    bizna = Buisness.objects.all()
    context = {
       
        'bizna':bizna
      }

    return render(request,'bizna.html', context)


@login_required
def bizna(request,pk):
    bizna=Buisness.objects.filter(id=pk)
    current_user=request.user
    return render(request, 'viewbizna.html', {"bizna":bizna})

def create_post(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('hood', hood.id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})
