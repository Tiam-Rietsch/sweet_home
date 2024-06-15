from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField()
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    neighbor_hood = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_picture/')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]