from django import forms
from .models import Investment, Land, Staff


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = '__all__'
        labels = {
            'date': 'তারিখ:',
            'Name': 'নিয়োগকারী নাম:',
            'quantity': 'পরিমাণ:',
            'other_info': 'অন্যান্য তথ্য:',
            'log': 'লগ:'
        }


class LandForm(forms.ModelForm):
    class Meta:
        model = Land
        fields = '__all__'
        labels = {
            'date': 'তারিখ:',
            'gher': 'ঘের:',
            'mousa': 'মৌজা:',
            'dag_number': 'দাগ নম্বর:',
            'khatian_number': 'খতিয়ান নম্বর:',
            'land_area': 'জমির আয়তন:',
            'cultivable_land': 'চাষযোগ্য জমি:',
            'adjacent_land': 'সহপাশের জমি/ক্যানাল:',
            'owners_name': 'মালিকের নাম:',
            'comments': 'মন্তব্য:',
            'log': 'লগ:'
        }


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        labels = {
            'date': 'তারিখঃ',
            'name': 'Enter name',
            'post': 'Enter post',
            'address': 'Enter address',
            'number': 'Enter number',
            'comments': 'মন্তব্য:',
            'log': 'লগ:'

        }
