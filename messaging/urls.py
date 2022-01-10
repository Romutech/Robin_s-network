from django.urls import path
from messaging import views

urlpatterns = [
    path('send/<receiver_id>', views.send_message, name='send_message'),
    path('read/<contact_id>', views.read_messages, name='read_messages'),
]
