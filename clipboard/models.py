from typing import Text
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Clipboard(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.text