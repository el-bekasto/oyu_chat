from rest_framework import authentication, permissions
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import *

import chat.models


class ListChats(ListAPIView):
    serializer_class = DialogsSerializer

    def get(self, request: Request, *args, **kwargs):
        result = DialogsSerializer(
            chat.models.Chat.objects.filter(participant_ids__contains=[request.user.pk]),
            many=True).data
        return Response(result)

