from django.urls import path, include

from .views import *

urlpatterns = [
    path('chats', ListChats.as_view(), name='get_chats'),
    path('chats/{chat_id}', GetChat.as_view())
]
