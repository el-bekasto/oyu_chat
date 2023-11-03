from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'first_name', 'created_at']


class ChatAdmin(admin.ModelAdmin):
    list_display = ['pk', 'chat_type', 'created_at']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'text', 'created_at']


admin.site.register(User, UserAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
