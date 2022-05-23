from django.db import models
from django.dispatch import receiver
from authentication.models import User
# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_received')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_sent')
    message = models.CharField(max_length=255)