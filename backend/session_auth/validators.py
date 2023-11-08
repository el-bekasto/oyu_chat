from rest_framework import serializers

from .serializers import *

import json


def validate_register(request_data):
    validation = RegisterFormSerializer(data=request_data)
    return validation.is_valid()
