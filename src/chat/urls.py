from django.urls import path
from .views import chat_sidebar, chat_view, chat_messages
from chat.views import chat_view
from .views import chat_sidebar
from . import views

urlpatterns = [
    path('', chat_view, name="chat"),
    path('<int:user_id>/', chat_messages, name="chat_messages"),
    path('chat/', chat_sidebar, name='chat_sidebar'),
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]
