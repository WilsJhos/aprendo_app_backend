from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import GameSection
from .serializers import GameSectionSerializer
from django.http import HttpResponseRedirect, HttpResponseForbidden
import os

@login_required
def index(request):
    sections = GameSection.objects.all()
    return render(request, 'index.html', {'sections': sections})

@login_required
def game_detail(request, id_name):
    game = get_object_or_404(GameSection, id_name=id_name)
    return render(request, f'games/{game.file_name}', {'game': game})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# API Views for Flutter
class GameSectionListAPI(generics.ListAPIView):
    queryset = GameSection.objects.all()
    serializer_class = GameSectionSerializer
    permission_classes = [] # Allow public access for now or change to IsAuthenticated
