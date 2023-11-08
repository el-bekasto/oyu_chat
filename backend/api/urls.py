from django.urls import path, include

from .views import *

urlpatterns = [
    path('getDialogs', ListDialogs.as_view(), name='get_dialogs'),
]
