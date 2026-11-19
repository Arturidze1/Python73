from django.db import models

from core.models import DateTimeMixin

class ProductBooking(DateTimeMixin):
    product = models.ForeignKey(
        to='Product',
        related_name='product_to_products',
        on_delete=models.CASCADE
    )

    booking = models.ForeignKey(
        to='Booking',
        related_name='products_to_book',
        on_delete = models.CASCADE
    )
    quantity = models.PositiveIntegerField(null=True)
    total_price = models.FloatField(null=True)

    class Meta:
        db_table = 'Product_bookings'
        verbose_name = 'Товар в бронировании'
        verbose_name_plural = 'Товары в бронировании'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.product} -> {self.booking}'