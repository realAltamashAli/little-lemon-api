from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # LittleLemonAPI endpoints
    path('api/', include('LittleLemonAPI.urls')),

    # Djoser authentication endpoints
    path('auth/', include('djoser.urls')),          # user management
    path('auth/', include('djoser.urls.authtoken')) # token login
]
