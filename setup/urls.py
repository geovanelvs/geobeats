from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # Para Login/Logout
    path('', lambda r: redirect('music_list')), # Redireciona a home para a lista
]