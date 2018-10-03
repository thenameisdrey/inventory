from django import forms

from .models import StockDetails, NewStock
    
class NewStockForm(forms.ModelForm):
    class Meta:
        model = NewStock
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Category name',
            'aria-label' : 'Todo', 'aria-describedby' : 'add-btn' }),
        }

class StockDetailsForm(forms.ModelForm):
    class Meta:
        model = StockDetails
        fields = ['category', 'name_of_item', 'qty_at_hand', 'cost_price', 'sales_price', 're_order']
        widgets = {
            'name_of_item' : forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Name of item',
            'aria-label' : 'Todo', 'aria-describedby' : 'add-btn' }),
            'qty_at_hand' : forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Quantity at hand',
            'aria-label' : 'Todo', 'aria-describedby' : 'add-btn' }),
            'sales_price' : forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Sales price',
            'aria-label' : 'Todo', 'aria-describedby' : 'add-btn' }),
            'cost_price' : forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Cost price',
            'aria-label' : 'Todo', 'aria-describedby' : 'add-btn' }),
            're_order' : forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Re-order',
            'aria-label' : 'Todo', 'aria-describedby' : 'add-btn' })
        }
   