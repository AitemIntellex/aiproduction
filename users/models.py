from django.contrib.auth.models import AbstractUser
from django.db import models
import hashlib

class CustomUser(AbstractUser):

    full_name = models.CharField(max_length=40, blank=True, null=True)
    display_name = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    social_links = models.JSONField(default=dict)
    interests = models.JSONField(default=list)
    avatar_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.avatar_url:
            self.avatar_url = f"https://www.gravatar.com/avatar/{hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()}?s=256&d=identicon"
        super().save(*args, **kwargs)
