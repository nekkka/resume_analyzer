# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        SEEKER = 'seeker', 'Job Seeker'
        RECRUITER = 'recruiter', 'Recruiter'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.SEEKER)

    def __str__(self):
        return f"{self.username} ({self.role})"
