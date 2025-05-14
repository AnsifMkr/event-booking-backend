from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from events.views import CustomTokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return JsonResponse({"message": "Event Booking API is running ✅"})
    
urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('events.urls')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
