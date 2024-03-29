from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description', 'category','image','price','quantity']

class OrderForm(forms.ModelForm):
    '''def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product', None)  # Get the product instance
        super(OrderForm, self).__init__(*args, **kwargs)'''

    class Meta:
        model = Order
        fields = ['quantity']

'''    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        product = self.product  # Assuming you pass the product instance to the form
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be a positive integer.")
        if quantity > product.quantity:
            raise forms.ValidationError("Insufficient stock for this quantity.")
        return quantity'''

class OrderUpdationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        