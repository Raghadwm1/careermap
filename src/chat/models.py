from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.sender} to {self.receiver}: {self.message}"
from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)  # User who sent the message
    room_name = models.CharField(max_length=100)  # Chat room identifier
    message = models.TextField()  # The actual message text
    timestamp = models.DateTimeField(auto_now_add=True)  # Time the message was sent

    def __str__(self):
        return f"{self.sender}: {self.message[:50]}..."

