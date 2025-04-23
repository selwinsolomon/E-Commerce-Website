from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product_name', 'quantity', 'amount', 'customer_email', 'address']

    def __init__(self, *args, **kwargs):
        product_name = kwargs.pop('product_name', None)
        amount = kwargs.pop('amount', None)
        super(OrderForm, self).__init__(*args, **kwargs)

        if product_name:
            self.fields['product_name'].initial = product_name
            self.fields['product_name'].widget.attrs['readonly'] = True

        if amount:
            self.fields['amount'].initial = amount
            self.fields['amount'].widget.attrs['readonly'] = True

