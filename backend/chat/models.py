from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<chatUser {self.username}>'


class Chat(models.Model):
    PRIVATE = 'private'
    GROUP = 'group'
    CHAT_TYPE_CHOICES = [
        (PRIVATE, 'Private'),
        (GROUP, 'Group')
    ]
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True)
    description = models.CharField(default=None, blank=True)
    chat_type = models.CharField(
        choices=CHAT_TYPE_CHOICES,
        default=PRIVATE
    )
    avatar = models.FileField(upload_to='avatars/%Y/%m/%d', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<Chat {self.name}>'


class Participant(models.Model):
    MEMBER = 'member'
    OWNER = 'owner'
    ADMIN = 'admin'
    RESTRICTED = 'restricted'
    LEFT = 'left'
    BANNED = 'banned'
    PARTICIPANT_TYPE_CHOICES = [
        (MEMBER, 'Member'),
        (OWNER, 'Owner'),
        (ADMIN, 'Admin'),
        (RESTRICTED, 'Restricted'),
        (LEFT, 'Left'),
        (BANNED, 'Banned')
    ]
    participant_type = models.CharField(choices=PARTICIPANT_TYPE_CHOICES, default=MEMBER)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_participants')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='participants')

    def __str__(self):
        return f'<Participant {self.user.username}>'


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    attachment = models.FileField(upload_to='attachments/%Y/%m/%d', blank=True)
    reply_to = models.ForeignKey('self', on_delete=models.PROTECT, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
