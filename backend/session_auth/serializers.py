from rest_framework import serializers


class LoginFormSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class RegisterFormSerializer(serializers.Serializer): # noqa
    username = serializers.CharField(required=True, max_length=100)
    password = serializers.CharField(required=True, min_length=8)
    re_password = serializers.CharField(required=True)
