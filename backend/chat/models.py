from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Модель пользователя. Наследуется от пользователя Django для аутентификации
    """
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<chatUser {self.username}>'


class Chat(models.Model):
    """
    Модель чата
    Attributes:
        name (str): название чата
        username (str): юзернейм, адрес чата
        description (str): описание чата
        chat_type (models.CharField): тип чата (группа или личный)
        avatar (models.FileField): аватарка чата
        updated_at (datetime): дата создания
        created_at (datetime): дата последнего обновления
    """
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
    """
    Модель участника. Нужен для связывания User и Chat
    Attributes:
        participant_type (str): тип участника (админ, участник, заблоканный etc.)
        user (User): пользователь
        chat (Chat): чат
        updated_at (datetime): дата создания
        created_at (datetime): дата последнего обновления
    """
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
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<Participant {self.user.username}>'


class Message(models.Model):
    """
    Модель сообщения
    Attributes:
        author (User): автор сообщения
        chat (Chat): чат, в котором размещено сообщение
        text (str): текст сообщения
        attachment (models.FileField): вложение сообщения. Пока только одно
        (нужно будет вывести в отдельную модель и связать с сообщением через relations)
        reply_to (Message): если не нуль, значит отвечает на другое сообщение
        updated_at (datetime): дата создания
        created_at (datetime): дата последнего обновления
    """
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    attachment = models.FileField(upload_to='attachments/%Y/%m/%d', blank=True)
    reply_to = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
