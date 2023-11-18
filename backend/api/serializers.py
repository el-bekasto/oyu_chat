from rest_framework.serializers import ModelSerializer
from chat.models import *


class ChatsSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'username', 'description', 'chat_type', 'updated_at', 'created_at']
