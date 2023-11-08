from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('session_auth/', include('session_auth.urls')),
    path('auth/', include('rest_framework.urls')),
]
