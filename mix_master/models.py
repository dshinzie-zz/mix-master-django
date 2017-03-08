from django.db import models
from django.utils import timezone

class Artist(models.Model):
    name = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
