from rest_framework import authentication, permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .serializers import *
from chat.models import Chat, Participant


class ListChatsView(ListAPIView):
    """
    Получить список чатов пользователя
    """
    serializer_class = ChatListChatSerializer

    def get_queryset(self):
        user_chats = [p.chat.pk for p in Participant.objects.select_related('chat').filter(
            user_id=self.request.user.pk,
            participant_type__in=[Participant.MEMBER, Participant.OWNER, Participant.ADMIN]
        )]
        return Chat.objects.filter(id__in=user_chats)


class GetChatView(RetrieveAPIView):
    """
    Получить один чат
    """
    serializer_class = ChatListChatSerializer

    def get_object(self):
        return Chat.objects.get(id=int(self.kwargs['chat_id']))


class ChatMessagesView(ListAPIView):
    """
    Получить сообщения конкретного чата
    """
    serializer_class = MessagesSerializer

    def get_queryset(self):
        chat_id = int(self.kwargs['chat_id'])
        return Message.objects.filter(chat_id=chat_id, chat__participants__user_id=self.request.user.pk)
