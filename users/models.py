from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    neighbor_hood = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    def __str__(self):
        return self.username
    

class ProprietorProfile(models.Model):
    user = models.OneToOneField("User", on_delete= models.CASCADE, blank=True, null=True )
    cni_recto = models.ImageField(blank=True, null=True, upload_to="profile_picture/")
    cni_verso = models.ImageField(blank=True, null=True, upload_to="profile_picture/")
    facture_recto = models.ImageField(blank=True, null=True, upload_to="profile_picture/")
    facture_verso = models.ImageField(blank=True, null=True, upload_to="profile_picture/")
    status = models.CharField(max_length=50, blank=True, null=True)

class BuyerProfile(models.Model):
    user = models.OneToOneField("User", on_delete= models.CASCADE, blank=True, null=True)