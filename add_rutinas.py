import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aprendo_app_django.settings')
django.setup()

from core.models import GameSection

GameSection.objects.get_or_create(
    id_name='rutinas',
    defaults={
        'emoji': '📅',
        'title': 'Rutinas Diarias Inclusivas',
        'description': 'Identifica rutinas de la vida diaria: mañana, tarde y noche.',
        'tags': ['🗓 Rutinas', '✅ Inclusivo'],
        'color_class': 'c1',
        'file_name': 'rutinas.html',
        'nav_label': '📅 Rutinas'
    }
)
print("Game added successfully!")
