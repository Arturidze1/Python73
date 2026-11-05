from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class RatingMixin(models.Model):

    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(5),
                    MinValueValidator(1)],
        verbose_name='Оценка',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True