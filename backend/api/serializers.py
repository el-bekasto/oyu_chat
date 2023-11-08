from rest_framework.serializers import ModelSerializer
from chat.models import *


class DialogsSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'chat_type', 'participant_ids']
