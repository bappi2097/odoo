from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=255)
    tagline = models.TextField()
    def __str__(self) -> str:
        return self.name

