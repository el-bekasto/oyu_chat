from django.urls import path, include

from .views import *

urlpatterns = [
    path('chats', ListChatsView.as_view(), name='get_chats'),  # получение моих чатов
    path('chats/<int:chat_id>', GetChatView.as_view()),  # конкретный чат
    path('chats/<int:chat_id>/messages', ChatMessagesView.as_view())  # сообщения конкретного чата
]
