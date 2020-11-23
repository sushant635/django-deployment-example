from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    #create relationship
    user =models.OneToOneField(User,on_delete=models.CASCADE)

    # Add additional attributes
    portfolio_site = models.URLField(blank=True)
    Profile_pic = models.ImageField(upload_to= 'profile_pic',blank = True)

    def __str__(self):
        return self.user.username
    
