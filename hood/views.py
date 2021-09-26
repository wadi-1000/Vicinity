from django.shortcuts import render,redirect
from .models import Neighbourhood,Buisness,Post
from .forms import UploadNewNeighbourhood,UploadNewBuisness,PostForm
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


    
@login_required
def create_post(request):
    form=PostForm
    current_user=request.user

    if request.method =="POST":
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=current_user
            post.save()

        return redirect('viewhood')

    else:
        form=PostForm()

    return render(request, 'post.html', {"form":form})



@login_required
def viewPost(request):
    
    posts = Post.objects.all()
    context = {
       
        'posts':posts
      }

    return render(request,'posts.html', context)


@login_required
def searchBizna(request):
    
    if 'bizna' in request.GET and request.GET['bizna']:
        search_term=request.GET.get('bizna')
        searched_buisnesses=Buisness.search_by_name(search_term)
        message=f"{search_term}"

        return render(request, "searchb.html", {"bizna":searched_buisnesses, "message":message})
    else:
        message="You have not searched for any buissness"
        return render(request, "searchb.html")

@login_required
def searchHood(request):
    
    if 'hood' in request.GET and request.GET['hood']:
        search_term=request.GET.get('hood')
        searched_hoods=Neighbourhood.search_by_hood(search_term)
        message=f"{search_term}"

        return render(request, "searchh.html", {"hood":searched_hoods, "message":message})
    else:
        message="You have not searched for any hoods"
        return render(request, "searchh.html")