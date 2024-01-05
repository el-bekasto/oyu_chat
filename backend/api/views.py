from rest_framework import authentication, permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import *
from chat.models import Chat, Participant


class ListChats(ListAPIView):
    def get(self, request: Request, *args, **kwargs):
        user_chats = [p.chat.pk for p in Participant.objects.select_related('chat').filter(
            user_id=request.user.pk,
            participant_type__in=[Participant.MEMBER, Participant.OWNER, Participant.ADMIN]
        )]
        result = ChatListChatSerializer(
            Chat.objects.filter(id__in=user_chats),
            many=True
        ).data
        return Response(result)


class GetChat(RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ChatListChatSerializer

    def get_object(self):
        return Chat.objects.get(id=int(self.kwargs['chat_id']))
