from django import forms
from booking_manager.models import ProductBooking


class ProductBookingForm(forms.ModelForm):
    class Meta:
        model = ProductBooking
        fields = ['product', 'quantity']

    def clean(self):
        clean_obj = super().clean()
        quantity = clean_obj.get('quantity')
        product = clean_obj.get('product')

        if product and quantity:
            if quantity > product.amount:
                self.add_error('quantity', f'Товаров мало на складе. Осталось {product.amount}')

            elif quantity <= 0:
                self.add_error('qauntity', 'Введите количество больше чем 0')

        return clean_obj




