from django.urls import path

from . import views


urlpatterns = [
    path('', views.property_list_view, name='property-list'),
    path("property/create/", views.property_create_view, name="create-property"),
    path('property/<int:pk>/', views.property_detail_view, name='property-detail')
]