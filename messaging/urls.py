from django.urls import path
from user_profile import views

urlpatterns = [
    path('', views.messaging, name='messaging'),
]
