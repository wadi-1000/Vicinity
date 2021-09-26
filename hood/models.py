from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Neighbourhood(models.Model):
    hood = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    pic = CloudinaryField('image')
    description = models.TextField()
    hospital_number = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)
    occupant_count = models.IntegerField(null=True, blank=True)
    admin = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
            return ( self.hood)
    def create_neighbourhood(self):
        self.save()
    
    def delete_neighbourhood(self):
        self.delete()

    def search_by_hood(search_term):
        hood=Neighbourhood.objects.filter(hood__icontains=search_term)
        return hood


class Buisness(models.Model):
   name = models.CharField(max_length = 100)
   owner = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
   hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,null=True)
   image = CloudinaryField('image')
   description = models.TextField()
   email = models.EmailField(default = "Please put in your buisness email address")

   def create_buisness(self):
        self.save()
    
   def delete_buisness(self):
        self.delete()

   def search_by_name(search_term):
        bizna=Buisness.objects.filter(name__icontains=search_term)
        return bizna

class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    post = models.TextField()
    image = CloudinaryField('image')
    date = models.DateTimeField(auto_now_add=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} Post'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()