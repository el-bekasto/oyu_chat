from rest_framework.serializers import ModelSerializer, SerializerMethodField
from chat.models import Chat, Message


class ChatListChatSerializer(ModelSerializer):
    """
    Сериалайзер для получения чата в списке чатов
    """
    class Meta:
        model = Chat
        fields = ['id', 'name', 'username', 'description', 'chat_type', 'avatar', 'created_at']


class OpenChatSerializer(ModelSerializer):
    """
    Сериалайзер для...хз
    """
    last_messages = SerializerMethodField

    def get_last_messages(self):
        return

    class Meta:
        model = Chat
        fields = ['id', 'name', 'username', 'description', 'chat_type', 'avatar', 'created_at']


class MessagesSerializer(ModelSerializer):
    """
    Сериалайзер для сообщений конкретного чата
    """
    class Meta:
        model = Message
        fields = ['id', 'author', 'chat', 'text', 'attachment', 'reply_to', 'created_at', 'updated_at']
        depth = 1
