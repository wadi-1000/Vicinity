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
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='hood')
    def create_neighbourhood(self):
        self.save()
    
    def delete_neighbourhood(self):
        self.delete()
