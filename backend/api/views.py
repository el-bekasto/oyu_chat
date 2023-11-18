from rest_framework import authentication, permissions
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import *
from chat.models import Chat, Participant


class ListChats(ListAPIView):
    def get(self, request: Request, *args, **kwargs):
        user_chats = [p.chat.pk for p in Participant.objects.filter(
            user_id=request.user.pk,
            participant_type__in=[Participant.MEMBER, Participant.OWNER, Participant.ADMIN]
        )]
        result = ChatsSerializer(
            Chat.objects.filter(id__in=user_chats),
            many=True
        ).data
        return Response(result)

