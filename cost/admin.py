from django.contrib import admin
from django.utils import timezone

from .models import FishPurchase, DailyCost, Salary


class FishbuyAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'fish_name', 'purchase_place', 'quantity', 'fish_count', 'price', 'log')
    list_filter = ('date', 'fish_name', 'purchase_place')
    search_fields = ('date', 'fish_name', 'purchase_place')
    ordering = ('-date',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.submitted_by = request.user
            obj.log = f" {request.user.username} - {timezone.now()}"
        super().save_model(request, obj, form, change)


admin.site.register(FishPurchase, FishbuyAdmin)


class DailycostAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'expenditure_sector', 'item_name', 'quantity', 'unit', 'cost_amount',
        'spender')
    list_filter = ('date', 'expenditure_sector')
    search_fields = ('date', 'item_name', 'spender__username')
    ordering = ('-date',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.submitted_by = request.user
            obj.log = f" {request.user.username} _ {timezone.now()}"
        super().save_model(request, obj, form, change)


admin.site.register(DailyCost, DailycostAdmin)


class SalaryAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'purpose', 'reason', 'quantity', 'rate', 'personel', 'total', 'voucher',
                                                                              'log')
    list_filter = ('date', 'purpose')
    search_fields = ('date', 'quantity', 'total')
    ordering = ('-date',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.submitted_by = request.user
            obj.log = f" {request.user.username} _ {timezone.now()}"
        super().save_model(request, obj, form, change)


admin.site.register(Salary, SalaryAdmin)
