from django.urls import path 

from . import views


urlpatterns = [
    path("program/", views.program_visit_view, name = "program-visit"),
    # path("cancel/<int:pk>/visit", cancelvisit, name= "cancelvisit")
]
