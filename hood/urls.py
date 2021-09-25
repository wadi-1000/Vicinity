from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('add_hood/',views.uploadNeighbourhood, name = 'add_hood'),
    path('viewhood/',views.viewHood, name = 'viewhood'),
    path('hood/<int:pk>/',views.hood, name = 'hood'),
    path('add_bizna/',views.uploadBuisness, name = 'add_bizna'),
    path('bizna/',views.viewBizna, name = 'view_bizna'),
]