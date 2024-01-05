from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class ChatAdmin(admin.ModelAdmin):
    """
    Модель админки для модели Чата
    """
    list_display = ['pk', 'chat_type', 'created_at']


class MessageAdmin(admin.ModelAdmin):
    """
    Модель админки для модели Сообщений
    """
    list_display = ['pk', 'author', 'text', 'created_at']


class ParticipantAdmin(admin.ModelAdmin):
    """
    Модель админки для модели Участника
    """
    list_display = ['pk', 'user', 'participant_type']


admin.site.register(User, UserAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Participant, ParticipantAdmin)
