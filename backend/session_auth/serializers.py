from rest_framework import serializers


class RegisterFormSerializer(serializers.Serializer): # noqa
    username = serializers.CharField(required=True, max_length=100)
    password = serializers.CharField(required=True, min_length=8)
    re_password = serializers.CharField(required=True)
