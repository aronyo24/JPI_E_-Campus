from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class FishPurchase(models.Model):
    date = models.DateField(verbose_name='তারিখ')
    fish_name = models.CharField(max_length=50, verbose_name='মাছের নাম')
    purchase_place = models.CharField(max_length=100, verbose_name='ক্রয়ের স্থান', blank=True,
                                      null=True)  # Allow blank values
    quantity = models.FloatField(verbose_name='পরিমাণ')
    fish_count = models.IntegerField(verbose_name='মাছের সংখ্যা')
    price = models.FloatField(verbose_name='মূল্য')
    ghere = models.CharField(max_length=50, verbose_name='পরিশোধের পদ্ধতি')
    voucher = models.CharField(max_length=50, verbose_name='ভাউচার')
    comment = models.TextField(verbose_name='মন্তব্য', blank=True, null=True)
    other_info = models.TextField(verbose_name='অন্য বিশেষ তথ্য', blank=True, null=True)
    log = models.CharField(max_length=800, verbose_name='লগ', blank=True)  # Make the log field blank

    class Meta:
        verbose_name = 'মাছ ক্রয়'
        verbose_name_plural = 'মাছ ক্রয় তথ্য'

    def __str__(self):
        return f'{self.date} - {self.fish_name} - {self.purchase_place} - {self.log}'


class DailyCost(models.Model):
    date = models.DateField(verbose_name='তারিখ')
    expenditure_sector = models.CharField(max_length=100, verbose_name='ব্যায়ের খাত')
    item_name = models.CharField(max_length=100, verbose_name='দ্রব্যের নামঃ')
    quantity = models.FloatField(verbose_name='পরিমাণ')
    unit = models.CharField(max_length=50, verbose_name='ইউনিট')
    cost_amount = models.FloatField(verbose_name='খরচের পরিমাণ')
    spender = models.CharField(max_length=100, verbose_name='খরচকারী')
    voucher = models.CharField(max_length=100, verbose_name='ভাউচার', blank=True)
    comment = models.TextField(verbose_name='মন্তব্য', blank=True, null=True)
    log = models.CharField(max_length=800, verbose_name='লগ', blank=True)

    class Meta:
        verbose_name = 'নৈমিত্তিক ব্যয়'
        verbose_name_plural = 'নৈমিত্তিক ব্যয় তথ্য'

    def __str__(self):
        return f'{self.date} - {self.expenditure_sector} - {self.item_name}'


class Salary(models.Model):
    date = models.DateField(verbose_name='তারিখঃ')
    purpose = models.CharField(verbose_name='ক্ষেত্র:', max_length=80, blank=True, null=True)
    reason = models.CharField(verbose_name='Reason:', max_length=100,blank=True, null=True)
    quantity = models.IntegerField(verbose_name='Quantity:',blank=True, null=True)
    rate = models.FloatField(verbose_name='Rate:', blank=True, null=True)
    personel = models.CharField(verbose_name='Personel:', max_length=100, null=True,blank=True,)
    total = models.FloatField(verbose_name='Total:', null=True,blank=True,)
    voucher = models.CharField(max_length=100, verbose_name='ভাউচার', blank=True, null=True)
    comment = models.TextField(verbose_name='মন্তব্য', blank=True, null=True)
    log = models.CharField(max_length=800, verbose_name='লগ', blank=True)

    class Meta:
        verbose_name = 'বেতন/শ্রমিক'
        verbose_name_plural = 'বেতন/শ্রমিক তথ্য '

    def __str__(self):
        return f'{self.date} - {self.purpose} - {self.reason}'
