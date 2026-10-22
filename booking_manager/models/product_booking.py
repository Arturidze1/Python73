from django.db import models

from core.models import BaseModel

class ProductBooking(BaseModel):
    product = models.ForeignKey(
        to='Product',
        on_delete=models.CASCADE
    )

    booking = models.ForeignKey(
        to='Booking',
        on_delete = models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    total_price = models.FloatField()

    class Meta:
        db_table = 'Product_bookings'
        verbose_name = 'Товар в бронировании'
        verbose_name_plural = 'Товары в бронировании'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.product} -> {self.booking}'