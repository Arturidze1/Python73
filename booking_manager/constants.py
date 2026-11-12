from django.db import models

class CategoryChoices(models.TextChoices):
    MASSAGE = 'Massage'
    MOUSTACHE = 'Moustache'
    BEARD = 'Beard'
    HAIRCUT = 'Haircut'