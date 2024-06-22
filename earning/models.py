from django.db import models


class Earning(models.Model):
    date = models.DateField(verbose_name="Date")
    sector = models.CharField(max_length=100, verbose_name='Sector')
    item = models.CharField(max_length=100, verbose_name='Item',blank=True, null=True)
    source = models.CharField(max_length=100, verbose_name='Source')
    quantity_per_unit = models.FloatField(verbose_name='Quantity Per Unit')
    quantity = models.FloatField(verbose_name='Quantity')
    unit = models.CharField(max_length=100, verbose_name='Unit', blank=True, null=True)
    price = models.FloatField(verbose_name='Price', blank=True, null=True)
    memo = models.TextField(verbose_name='Memo', blank=True, null=True)
    comment = models.CharField(max_length=100, verbose_name='Comment', blank=True, null=True)
    log = models.CharField(max_length=800, verbose_name='Log', blank=True)

    def __str__(self):
        return f"{self.date} - {self.item} - {self.sector}"
