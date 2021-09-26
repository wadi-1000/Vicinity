from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('add_hood/',views.uploadNeighbourhood, name = 'add_hood'),
    path('viewhood/',views.viewHood, name = 'viewhood'),
    path('hood/<int:pk>/',views.hood, name = 'hood'),
    path('add_bizna/',views.uploadBuisness, name = 'add_bizna'),
    path('bizna/',views.viewBizna, name = 'view_bizna'),
    path('viewbizna/<int:pk>/',views.bizna, name = 'bizna'),
    path('post/',views.create_post, name = 'post'),
    path('posts/',views.viewPost, name = 'posts'),
    path('searchbizna/', views.searchBizna, name="search_results"),
    path('searchhood/', views.searchHood, name="search_res"),
    path('join_hood/<id>', views.join_neighbourhood, name='join-hood'),
    path('leave_hood/<id>', views.leave_neighbourhood, name='leave-hood'),
]