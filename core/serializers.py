from rest_framework import serializers
from .models import GameSection

class GameSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSection
        fields = ['id', 'id_name', 'emoji', 'title', 'description', 'tags', 'color_class', 'file_name', 'nav_label']
