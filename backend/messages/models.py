from django.db import models
from django.dispatch import receiver

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey()
    receiver = models.ForeignKey()
    message = models.CharField(max_length=255)