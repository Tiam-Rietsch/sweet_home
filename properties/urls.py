from django.urls import path

from . import views
from .views import createproperty, updateproperty


urlpatterns = [
    path('', views.property_list_view, name='property-list'),
    path("/createproperty", createproperty, name="createproperty"),
    path("update/<int:pk>/property", updateproperty, name= "updateproperety"),
    path("delete/<int:pk>/property", views.deleteproperty, name= "deleteproperty"),
]