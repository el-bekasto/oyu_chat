from django.urls import path, include

from .views import *

urlpatterns = [
    path('getChats', ListChats.as_view(), name='get_dialogs'),
]
