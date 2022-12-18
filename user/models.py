from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class ContactForm(models.Model):
    fullname= models.CharField(max_length=100)
    email= models.EmailField()
    contact= models.CharField(max_length=50)
    message= models.CharField(max_length=200)
    
    
class ServiceForm(models.Model):
    cname= models.CharField(max_length=100)
    cemail= models.EmailField()
    ccontact= models.CharField(max_length=50)
    cdate= models.DateField(max_length=200)
    clocation=models.CharField(max_length=200)
    cservice= models.CharField(max_length=200)
    
    
#    
#    def __str__(self):
#        return self.name
#
#

#
#class CustomUser(AbstractUser):
#    pass
#    # add additional fields in here
#
#    def __str__(self):
#        return self.usernam
#