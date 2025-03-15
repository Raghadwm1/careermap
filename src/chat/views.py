from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User

@login_required
def chat_view(request):
    users = User.objects.exclude(id=request.user.id)  # Show all users except the logged-in one
    return render(request, "chat/chat.html", {"users": users})

@login_required
def chat_messages(request, user_id):
    user = request.user
    other_user = User.objects.get(id=user_id)
    messages = Message.objects.filter(
        sender__in=[user, other_user],
        receiver__in=[user, other_user]
    ).order_by("timestamp")
    return render(request, "chat/messages.html", {"messages": messages, "receiver": other_user})


@login_required
def chat_sidebar(request):
    user = request.user
    messages = Message.objects.filter(receiver=user).order_by('-timestamp')[:10]
    return render(request, 'chat/chat_sidebar.html', {'messages': messages})

def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})