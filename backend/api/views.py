from rest_framework import authentication, permissions
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import *
from chat.models import Chat


class ListChats(ListAPIView):
    serializer_class = DialogsSerializer

    def get(self, request: Request, *args, **kwargs):
        result = DialogsSerializer(
            Chat.objects.filter(participants__user_id=request.user.pk),
            many=True).data
        return Response(result)

