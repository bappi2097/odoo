from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    def __str__(self) -> str:
        return self.name
