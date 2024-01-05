from django.urls import path
from .views import *

urlpatterns = [
    path('register/', SignupView.as_view(), name='register'),  # регистрация
    path('csrf/', GetCSRFTokenView.as_view(), name='csrf_cookie'),  # получить csrf
    path('login/', LoginView.as_view(), name='login'),  # log into account
    path('logout/', LogoutView.as_view(), name='logout'),  # log out from account
    path('authenticated/', CheckAuthenticatedView.as_view(), name='checkauth')  # check if i'm authenticated
]
