from django.urls import path

from . import views

urlpatterns = [
    path('', views.property_list_view, name='property-list'),
]