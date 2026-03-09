from django.contrib import admin
from .models import GameSection

@admin.register(GameSection)
class GameSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_name', 'emoji')
    search_fields = ('title', 'description')
