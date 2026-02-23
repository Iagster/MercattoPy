from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'stock',
            'is_active',
            'category',
        ]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name.strip()) < 3:
            raise forms.ValidationError(
                'O nome do produto deve ter pelo menos 3 caracteres.'
            )
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError(
                'O preço não pode ser negativo.'
            )
        return price

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError(
                'O estoque não pode ser negativo.'
            )
        return stock

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if category and not category.is_active:
            raise forms.ValidationError(
                'Não é possível usar uma categoria inativa.'
            )
        return category