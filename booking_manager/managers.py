import datetime
from django.db import models

class GetActive(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, visit_time__gt=datetime.datetime.today())
