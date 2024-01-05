from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Swagger',
        default_version='v1',
        description='OYU CHAT api documentation.'
    ),
    public=True,
    permission_classes=[AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),  # админка
    path('api/', include('api.urls')),  # пути апи
    path('auth/', include('session_auth.urls')),  # пути аутентификации
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')  # сваггер
]
