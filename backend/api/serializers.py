from rest_framework.serializers import ModelSerializer, SerializerMethodField
from chat.models import *


class ChatListChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'username', 'description', 'chat_type', 'avatar', 'created_at']


class OpenChatSerializer(ModelSerializer):
    last_messages = SerializerMethodField

    def get_last_messages(self):
        return

    class Meta:
        model = Chat
        fields = ['id', 'name', 'username', 'description', 'chat_type', 'avatar', 'created_at']
