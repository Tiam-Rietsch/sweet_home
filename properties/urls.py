from django.urls import path

from . import views
from .views import createproperty, updateproperty


urlpatterns = [
    path('', views.property_list_view, name='property-list'),
    path("property/create/", createproperty, name="create-property"),
    path("property/update/<int:pk>/property", updateproperty, name= "update-properety"),
    path("property/delete/<int:pk>/property", views.deleteproperty, name= "delete-property"),
    path('property/<int:pk>/', views.property_detail_view, name='property-detail')
]