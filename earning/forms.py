from django import forms
from .models import Earning

class EarningForm(forms.ModelForm):
    class Meta:
        model = Earning
        fields = '__all__'
        labels = {
            'date': 'Date:',
            'sector': 'Sector:',
            'item': 'Item:',
            'source': 'Source:',
            'quantity_per_unit': 'Quantity Per Unit:',  # Removed leading space
            'quantity': 'Quantity',
            'unit': 'unit',
            'price': 'Price:',
            'memo': 'Memo',
            'comment': 'মন্তব্য:',
            'log': 'লগ:'
        }
