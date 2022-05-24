from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass 

class Deal(models.Model):
    contact_person = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    value = models.IntegerField(default=0)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
