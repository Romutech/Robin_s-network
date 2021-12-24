from django.urls import path
from user_profile import views

urlpatterns = [
    path('', views.read_profile_view, name='profile')
]
