from django.urls import path
from .views import *

urlpatterns = [
    path('register', SignupView.as_view(), name='register'),
    path('csrf_cookie/', GetCSRFTokenView.as_view(), name='csrf_cookie')
]
