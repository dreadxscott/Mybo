from django.db import models
from django.contrib.auth.models import AbstractUser
from japanese_learner.models import Word

class CustomUser(AbstractUser):
    # Additional fields for the user
    points = models.IntegerField(default=0)  # Integer field for points
    level = models.CharField(max_length=50, default="Beginner")  # CharField for user level
    mastered_words = models.ManyToManyField(Word, blank=True)  # Many-to-many relationship with Word

    

    def __str__(self):
        return self.username