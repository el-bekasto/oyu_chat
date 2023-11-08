from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from chat.models import User


@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = self.request.data

        username = data['username']
        password = data['password']
        re_password = data['re_password']

        if re_password != password:
            return Response({'error': 'Passwords do not match!'}, status=401)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'This username already exists!'}, status=409)
        if len(password) < 8:
            return Response({'erorr': 'Minimum password size is 8 symbols!'}, status=401)
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response({'ok': 'User created successfully!'}, status=201)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFTokenView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        return Response({'ok': 'CSRF cookie set'})
