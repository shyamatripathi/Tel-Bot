
# Create your models here.
from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    chat_id = models.BigIntegerField()


