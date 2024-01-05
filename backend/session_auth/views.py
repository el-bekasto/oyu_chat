from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from chat.models import User

from . import validators


@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    """
    Вью для регистрации
    """
    permission_classes = (AllowAny,)

    def post(self, request: Request):
        """
        Метод для регистрации
        :param request: запрос
        :return: 401 or 409 or 201
        """
        # тело запроса, форма
        data = self.request.data

        # валидируем
        if not validators.validate_register(data):
            return Response({'details': 'Bad Request Body'}, status=status.HTTP_400_BAD_REQUEST)

        username = data['username']
        password = data['password']
        re_password = data['re_password']

        # если повтор пароля не совпадает, возвращаем 401
        if re_password != password:
            return Response({'error': 'Passwords do not match!'}, status=status.HTTP_401_UNAUTHORIZED)
        # если пользователь с таким юзернеймом уже есть, возвращаем 409
        if User.objects.filter(username=username).exists():
            return Response({'error': 'This username already exists!'}, status=status.HTTP_409_CONFLICT)
        # если пароль слишком короткий, возвращаем 401
        if len(password) < 8:
            return Response({'erorr': 'Minimum password size is 8 symbols!'}, status=status.HTTP_401_UNAUTHORIZED)
        # создаем и возвращаем 201
        User.objects.create_user(username=username, password=password)
        return Response({'ok': 'User created successfully!'}, status=status.HTTP_201_CREATED)


@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    """
    Вью для входа в аккаунт
    """
    permission_classes = (AllowAny, )

    def post(self, request):
        """
        Метод входа в аккаунт
        :param request: запрос
        :return: 400 или 200 или 401
        """
        # тело запроса
        data = self.request.data

        # проходим валидацию формы входа
        if not validators.validate_login(data):
            return Response({'details': 'Bad Request Body'}, status=status.HTTP_400_BAD_REQUEST)

        username = data['username']
        password = data['password']

        # пробуем войти с переданными данными
        user = authenticate(username=username, password=password)
        if user:
            # успешный вход
            login(request, user)
            return Response({'ok': 'You logged in successfully!'}, status=status.HTTP_200_OK)
        else:
            # ошибка
            return Response({'error': 'Your login or password is incorrect!'}, status=status.HTTP_401_UNAUTHORIZED)


@method_decorator(csrf_protect, name='dispatch')
class LogoutView(APIView):
    """
    Вьюха для выхода из аккаунта
    """
    def post(self, request):
        """
        Метод для выхода из аккаунта
        :param request: запрос
        :return: 200
        """
        logout(request)
        return Response({'ok': 'Logged out!'}, status=status.HTTP_200_OK)


class CheckAuthenticatedView(APIView):
    """
    Вьюха для проверки входа в аккаунт
    """
    permission_classes = (AllowAny, )

    def get(self, request):
        """
        Проверка аутентификации
        :param request: запрос
        :return: 200
        """
        if request.user.is_authenticated:
            return Response({'authenticated': True}, status=status.HTTP_200_OK)
        return Response({'authenticated': False}, status=status.HTTP_200_OK)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFTokenView(APIView):
    """
    Вьюха для получения csrf токена
    """
    permission_classes = (AllowAny, )

    def get(self, request): # noqa
        return Response({'ok': 'CSRF cookie set'})
