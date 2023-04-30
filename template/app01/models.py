from django.db import models


# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=10, default="name")
    email = models.TextField(max_length=50, default="email")
    phone = models.TextField(max_length=20, default="phone")
    message = models.TextField(max_length=150, default="message")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Message"
