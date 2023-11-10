from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from chat.models import User

from . import validators


@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = self.request.data

        if not validators.validate_register(data):
            return Response({'details': 'Bad Request Body'}, status=status.HTTP_400_BAD_REQUEST)

        username = data['username']
        password = data['password']
        re_password = data['re_password']

        if re_password != password:
            return Response({'error': 'Passwords do not match!'}, status=status.HTTP_401_UNAUTHORIZED)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'This username already exists!'}, status=status.HTTP_409_CONFLICT)
        if len(password) < 8:
            return Response({'erorr': 'Minimum password size is 8 symbols!'}, status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response({'ok': 'User created successfully!'}, status=status.HTTP_201_CREATED)


@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        data = self.request.data

        if not validators.validate_login(data):
            return Response({'details': 'Bad Request Body'}, status=status.HTTP_400_BAD_REQUEST)

        username = data['username']
        password = data['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'ok': 'You logged in successfully!'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Your login or password is incorrect!'}, status=status.HTTP_401_UNAUTHORIZED)


@method_decorator(csrf_protect, name='dispatch')
class LogoutView(APIView):
    def post(self, request):
        try:
            logout(request)
            return Response({'ok': 'Logged out!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'Something went wrong! {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@method_decorator(csrf_protect, name='dispatch')
class CheckAuthenticatedView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        if User.is_authenticated:
            return Response({'ok': 'You are authenticated!'}, status=status.HTTP_200_OK)
        return Response({'ok': 'You are not authenticated!'}, status=status.HTTP_200_OK)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFTokenView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request): # noqa
        return Response({'ok': 'CSRF cookie set'})
