from .serializers import *


def validate_register(request_data):
    """
    Валидация формы регистрации
    :param request_data: заполненная форма
    :return: валид не валид
    """
    return RegisterFormSerializer(data=request_data).is_valid()


def validate_login(request_data):
    """
    Валидация формы входа
    :param request_data: заполненная форма
    :return: валид не валид
    """
    return LoginFormSerializer(data=request_data).is_valid()
