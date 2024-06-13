from django.db import models

# Create your models here.
class Property(models.Model):
    land_title = models.FileField(upload_to='land_titles/')
    property_type = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    neighbohood = models.CharField(max_length=100)
    standing = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    price = models.BigIntegerField()
    description = models.TextField()
    
    class Meta:
        verbose_name = "propertie"
    