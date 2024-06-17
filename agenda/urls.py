from django.urls import path 
from .views import createvisit
from .views import cancelvisit


urlpatterns = [
    path("/createvisit", createvisit, name = "createview"),
    path("cancel/<int:pk>/visit", cancelvisit, name= "cancelvisit")
]
