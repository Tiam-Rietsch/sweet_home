from django import template
from django.contrib.auth.models import AnonymousUser

register = template.Library()

@register.filter(name='imageURL')
def imageURL(user):
    if not isinstance(user, AnonymousUser) and user.profile_picture:
        return user.profile_picture.url 
    else:
        return '/static/images/account.png'