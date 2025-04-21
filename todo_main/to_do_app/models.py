from django.db import models

# Create your models here.

class todo(models.Model):
    title = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    isCompleted = models.BooleanField(default=False)
    