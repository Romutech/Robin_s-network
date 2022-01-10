from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Conversation, Message


@login_required
def send_message(request, receiver_id):
    try:
        receiver_user = User.objects.get(id=receiver_id)
    except User.DoesNotExist:
        return redirect(request, 'read_profile', request.user.id)
    if request.method == 'POST':
        if len(request.POST.get('message')) == 0:
            return redirect('read_messages', receiver_id)
        try:
            conversation = Conversation.objects.get(
                user_1=request.user, user_2=receiver_user
            )
        except Conversation.DoesNotExist:
            try:
                conversation = Conversation.objects.get(
                    user_1=receiver_user, user_2=request.user
                )
            except Conversation.DoesNotExist:
                conversation = Conversation.objects.create(
                    user_1=request.user, user_2=receiver_user
                )
        Message.objects.create(
            conversation=conversation,
            author=request.user,
            receiver=receiver_user,
            message=request.POST.get('message')
        )
    return redirect('read_messages', receiver_id)


@login_required
def read_messages(request, contact_id):
    conversation = None
    try:
        receiver_user = User.objects.get(id=contact_id)
    except User.DoesNotExist:
        return redirect(request, 'read_profile', request.user.id)
    try:
        conversation = Conversation.objects.get(
            user_1=request.user, user_2=receiver_user
        )
    except Conversation.DoesNotExist:
        try:
            conversation = Conversation.objects.get(
                user_1=receiver_user, user_2=request.user
            )
        except Conversation.DoesNotExist:
            pass
    try:
        messages = conversation.messages.all()
    except:
        message = []
    return render(request, 'messaging/messaging.html', locals())
