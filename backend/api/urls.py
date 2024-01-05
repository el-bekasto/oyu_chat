from django.urls import path, include

from .views import *

urlpatterns = [
    path('chats', ListChatsView.as_view(), name='get_chats'),
    path('chats/<int:chat_id>', GetChatView.as_view()),
    path('chats/<int:chat_id>/messages', ChatMessagesView.as_view())
]
