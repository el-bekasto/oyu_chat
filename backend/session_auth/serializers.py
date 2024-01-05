from rest_framework import serializers


class LoginFormSerializer(serializers.Serializer): # noqa
    """
    Форма для входа в аккаунт
    Attributes:
        username (str): имя пользователя
        password (str): пароль пользователя
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class RegisterFormSerializer(serializers.Serializer): # noqa
    """
    Форма для регистрации
    Attributes:
        username (str): имя пользователя
        password (str): пароль пользователя
        re_password (str): повтор пароля
    """
    username = serializers.CharField(required=True, max_length=100)
    password = serializers.CharField(required=True, min_length=8)
    re_password = serializers.CharField(required=True)
