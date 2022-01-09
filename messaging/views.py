from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from user_profile.models import ProfilePicture
from .models import Conversation

from messaging.forms import MessageForm


@login_required
def messaging(request, user_receiver):
    picture_connected_user = ProfilePicture.get_profile_picture(request.user)
    form = MessageForm(request.POST or None)
    if form.is_valid():
        message = form.save(commit=False)
        try:
            conversation = Conversation.objects.get(
                user_1=request.user, user_2=message.receiver
            )
        except Conversation.DoesNotExist:
            try:
                conversation = Conversation.objects.get(
                    user_1=message.receiver, user_2=request.user
                )
            except Conversation.DoesNotExist:
                conversation = Conversation.objects.create(
                    user_1=request.user, user_2=message.receiver
                )
        message.conversation = conversation
        message.author = request.user
        message.save()
    return render(request, 'messaging/messaging.html', locals())
