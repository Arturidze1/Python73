from django.db import models

class ClientStatusChoices(models.TextChoices):
    NOOB = 'Noob'
    BEGINNER = 'Beginner'
    EXPERT = 'Expert'
    LEGEND = 'Legend'