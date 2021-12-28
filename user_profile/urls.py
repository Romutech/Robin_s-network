from django.urls import path
from user_profile import views

urlpatterns = [
    path('', views.read_profile, name='read_profile'),
    path('edit', views.create_or_update_profile, name='edit_profile')
]
