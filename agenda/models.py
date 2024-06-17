from django.db import models
from users.models import BuyerProfile
from properties.models import Property

class Visit(models.Model):

    date_1= models.DateTimeField(blank=True, null=True)
    date_2= models.DateTimeField(blank=True, null=True)
    date_3= models.DateTimeField(blank=True, null=True)
    buyer_profile =models.ForeignKey( BuyerProfile, on_delete=models.CASCADE, related_name='agenda')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='agenda')

    def __str__(self):
        return self.buyer_profile.user.username
    

