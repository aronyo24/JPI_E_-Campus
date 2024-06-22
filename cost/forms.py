from django import forms
from .models import FishPurchase, DailyCost, Salary


class FishPurchaseForm(forms.ModelForm):
    class Meta:
        model = FishPurchase
        fields = '__all__'

        labels = {
            'date': 'তারিখ',
            'fish_name': 'মাছের নাম',
            'purchase_place': 'ক্রয়ের স্থান',
            'quantity': 'পরিমাণ',
            'fish_count': 'মাছের সংখ্যা',
            'price': 'মূল্য',
            'payment_method': 'পরিশোধের পদ্ধতি',
            'voucher': 'ভাউচার',
            'comment': 'মন্তব্য',
            'other_info': 'অন্য বিশেষ তথ্য',
            'log': 'লগ',
        }


class DailyCostForm(forms.ModelForm):
    class Meta:
        model = DailyCost
        fields = '__all__'

        labels = {
            'date': 'তারিখ',
            'expenditure_sector': 'ব্যায়ের খাত',
            'item_name': '্রব্যের নামঃ',
            'quantity': 'পরিমাণ',
            'unit': 'ইউনিট',
            'cost_amount ': 'খরচের পরিমাণ',
            'spender': 'খরচকারী',
            'voucher': 'ভাউচার',
            'comment': 'মন্তব্য',
            'log': 'লগ',
        }


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'

        labels = {
            'date': 'তারিখ',
            'purpose': 'ক্ষেত্র',
            'reason': 'Reason',
            'quantity': 'পরিমাণ',
            'rate': 'হার',
            'personel': 'ব্যক্তি',
            'total': 'মোট',
            'voucher': 'ভাউচার',
            'comment': 'মন্তব্য',
            'log': 'লগ',

        }


