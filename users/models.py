from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords!
    name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    pronouns = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
