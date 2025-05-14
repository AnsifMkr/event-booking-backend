from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from events.views import CustomTokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static

def api_home(request):
    return HttpResponse("""
        <html>
            <head><title>API Status</title></head>
            <body style="font-family: Arial; text-align: center; margin-top: 50px;">
                <h1>✅ API is connected</h1>
                <p>Welcome to the Event Booking Backend</p>
            </body>
        </html>
    """)
    
urlpatterns = [
    path('', api_home),
    path('admin/', admin.site.urls),
    path('api/', include('events.urls')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
