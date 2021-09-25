from .models import Neighbourhood,Buisness
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