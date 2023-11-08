from .serializers import *


def validate_register(request_data):
    return RegisterFormSerializer(data=request_data).is_valid()


def validate_login(request_data):
    return LoginFormSerializer(data=request_data).is_valid()
