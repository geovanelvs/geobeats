from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicViewSet, PlaylistViewSet
from music import views

# Configuração da API
router = DefaultRouter()
# ADICIONAMOS O BASENAME AQUI NA LINHA ABAIXO:
router.register(r'musicas', views.MusicViewSet, basename='music-api') 
router.register(r'playlists', PlaylistViewSet, basename='playlist-api')

urlpatterns = [
    # Rotas do CRUD (Visual)
    path('list/', views.music_list, name='music_list'),
    path('add/', views.music_add, name='music_add'),
    path('update/<int:pk>/', views.music_update, name='music_update'),
    path('delete/<int:pk>/', views.music_delete, name='music_delete'),
    path('register/', views.register, name='register'),
    
    # Rota da API (JSON)
    path('api/', include(router.urls)),

    path('playlists/', views.playlist_list, name='playlist_list'),
    path('playlists/add/', views.playlist_add, name='playlist_add'),
    path('playlists/editar/<int:id>/', views.playlist_edit, name='playlist_edit'),
    path('playlists/apagar/<int:id>/', views.playlist_delete, name='playlist_delete'),
]