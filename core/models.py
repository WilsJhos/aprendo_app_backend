from django.db import models

class GameSection(models.Model):
    id_name = models.SlugField(unique=True)
    emoji = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.JSONField(default=list)
    color_class = models.CharField(max_length=20)
    file_name = models.CharField(max_length=100)
    nav_label = models.CharField(max_length=50)

    def __str__(self):
        return self.title
