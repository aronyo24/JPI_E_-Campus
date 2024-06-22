from django.contrib import admin
from django.utils import timezone

from .models import Earning


class EarningAdmin(admin.ModelAdmin):
    list_display = ('date', 'sector', 'item', 'source', 'quantity_per_unit', 'quantity', 'unit', 'price', 'memo', 'log')
    list_filter = ('date', 'price')
    search_fields = ('date', 'sector', 'item', 'price')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.log = f"{request.user}_{timezone.now()}"
        super().save_model(request, obj, form, change)


admin.site.register(Earning, EarningAdmin)
