from .models import Neighbourhood,Buisness,Post
from django.forms import ModelForm
from django import forms



class UploadNewNeighbourhood(forms.ModelForm):
    class Meta:
        model=Neighbourhood
        exclude=['occupant_count','admin']
        fields=['hood','location','pic','description','hospital_number','police_number']

class UploadNewBuisness(forms.ModelForm):
    class Meta:
        model=Buisness
        fields=['name','owner','hood','image','email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')