from django.urls import path
from user_profile import views

urlpatterns = [
    path('edit', views.create_or_update_profile, name='edit_profile'),
    path(
        'upload_profile_picture',
        views.upload_profile_picture,
        name='upload_profile_picture'
    ),
    path(
        'profile_picture/delete',
        views.delete_profile_picture,
        name='delete_profile_picture'
    ),
    path('<user_id>', views.read_profile, name='read_profile'),
]
