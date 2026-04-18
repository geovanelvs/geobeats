from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Configuração da API
router = DefaultRouter()
router.register(r'musicas', views.MusicViewSet)

urlpatterns = [
    # Rotas do CRUD (Visual)
    path('list/', views.music_list, name='music_list'),
    path('add/', views.music_add, name='music_add'),
    path('update/<int:pk>/', views.music_update, name='music_update'),
    path('delete/<int:pk>/', views.music_delete, name='music_delete'),
    path('register/', views.register, name='register'),
    
    # Rota da API (JSON)
    path('api/', include(router.urls)),
]