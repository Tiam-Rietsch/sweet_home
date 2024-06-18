from django.db import models
from users.models import (
    ProprietorProfile,
    BuyerProfile
)

# Create your models here.
class Property(models.Model):
    class Standing(models.TextChoices):
        PREMIUM = 'P', 'Premium'
        HIGH = 'H', 'Hight'
        STANDARD = 'S', 'Standard'
    
    
    class PropertyType(models.TextChoices):
        APARTMENT = 'A', 'Apartment'
        FURNISHED_APARTMENT = 'FA', 'Furnished Apartment'
        ROOM = 'R', 'Room'
        STUDIO = 'S', 'Studio'
    
    
    proprietor = models.ForeignKey(ProprietorProfile, on_delete=models.CASCADE, related_name='properties', blank=True, null=True)
    tenant = models.ForeignKey(BuyerProfile, on_delete=models.SET_NULL, related_name='properties', blank=True, null=True)
    land_title = models.FileField(upload_to='land_titles/')
    property_type = models.CharField(max_length=3, choices=PropertyType, default=PropertyType.APARTMENT)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    standing = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    price = models.BigIntegerField()
    description = models.TextField()
    standing = models.CharField(max_length=1, choices=Standing, default=Standing.STANDARD)
    
    class Meta:
        verbose_name = "propertie"
    
    
class PropertyRoom(models.Model):
    
    class RoomType(models.TextChoices):
        LIVING_ROOM = 'LVR', 'Living Room'
        BED_ROOM = 'BDR', 'Bed Room'
        KITCHEN = 'KIT', 'Kietchen'
        BALCONY = 'BAL', 'Balcony'
        
    property = models.ForeignKey('Property', on_delete=models.CASCADE, related_name='rooms')
    room_type = models.TextField(choices=RoomType, max_length=3, default=RoomType.LIVING_ROOM)
    image = models.ImageField(upload_to='property_rooms/')
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    
    def __str__(self):
        return f'{self.room_type} for {self.property.description[:15]} property'