from django.urls import path
from .views import *

urlpatterns = [
    path('register', SignupView.as_view(), name='register'),
    path('csrfCookie/', GetCSRFTokenView.as_view(), name='csrf_cookie'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('authenticated/', CheckAuthenticatedView.as_view(), name='checkauth')
]
