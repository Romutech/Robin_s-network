from django.contrib.auth.models import User
from django.db import models


class Conversation(models.Model):
    user_1 = models.ForeignKey(
        User, models.SET_NULL, blank=True, null=True, related_name="user_1"
    )
    user_2 = models.ForeignKey(
        User, models.SET_NULL, blank=True, null=True, related_name="user_2"
    )


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    author = models.ForeignKey(
        User, models.SET_NULL, blank=True, null=True, related_name="author"
    )
    receiver = models.ForeignKey(
        User, models.SET_NULL, blank=True, null=True, related_name="receiver"
    )
    message = models.TextField()
