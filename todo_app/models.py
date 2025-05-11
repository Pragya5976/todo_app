from django.db import models

# Create your models here.

class Task(models.Model):
    text = models.CharField(max_length=255, default='') 
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title
