from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

def ping_server(request):
    return JsonResponse({
        "message": "Ping!"
    })
urlpatterns = [
    # API schema endpoints (drf-spectacular)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Django admin interface
    path('admin/', admin.site.urls),

    # User API routes (authentication, registration, profile, etc.)
    path('api/', include('user_api.urls')),

    # Chat room WebSocket/API endpoints
    path('api/', include('chat_room.urls')),

    # Url for automatically ping the server so it doesn't sleep
    path('ping/', ping_server, name="ping")
]

# Serving media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
