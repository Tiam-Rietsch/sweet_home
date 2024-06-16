from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('proprietor/register/', views.become_proprietor_view, name='become-proprietor'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),
]