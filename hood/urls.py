from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('add_hood/',views.uploadNeighbourhood, name = 'add_hood'),
    path('viewhood/',views.viewhood, name = 'viewhood'),
]