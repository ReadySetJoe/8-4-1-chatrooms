from django.db import models
from django.utils import timezone


class Todo(models.Model):
    name = models.CharField(max_length=255)
    due = models.DateField(default=timezone.now())
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
