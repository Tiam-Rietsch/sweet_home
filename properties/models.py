from django.db import models

# Create your models here.
class Property(models.Model):
    proprietor = models.ForeignKey('ProprietorProfile', on_delete=models.CASCADE, related_name='properties')
    tenant = models.ForeignKey('BuyerProfile', on_delete=models.SET_NULL, related_name='properties')
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
    