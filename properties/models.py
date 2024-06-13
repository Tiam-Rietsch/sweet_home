from django.db import models

# Create your models here.
class Property_type(models.Model):
    land_title = models.FileField(upload_to='/land_titles/')
    types = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    neighborood = models.CharField(max_length=100)
    standing = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    price = models.BigIntegerField()
    description = models.TextField()
    