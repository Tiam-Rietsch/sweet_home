from django.contrib import admin
from .models import ProprietorProfile
from .models import BuyerProfile
from .models import User

admin.site.register(User)
admin.site.register(ProprietorProfile)
admin.site.register(BuyerProfile)
