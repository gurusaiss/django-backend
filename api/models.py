from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
