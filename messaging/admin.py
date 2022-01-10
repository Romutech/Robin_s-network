from django.contrib import admin

from messaging.models import Message, Conversation

admin.site.register(Conversation)
admin.site.register(Message)
