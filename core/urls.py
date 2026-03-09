from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<slug:id_name>/', views.game_detail, name='game_detail'),
    # API endpoints
    path('api/games/', views.GameSectionListAPI.as_view(), name='api_games'),
]
