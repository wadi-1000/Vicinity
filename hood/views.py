from django.shortcuts import render
from django.htpp import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')