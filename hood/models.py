from django.db import models
from django.contrib.auth import User
from cloudinary.models import CloudinaryField
from users.models import Profile

# Create your models here.
class Neighbourhood(models.Model):
    hood = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    occupants = models.PositiveIntegerField(default = 0)
    
    def create_neighbourhood(self):
        self.save()