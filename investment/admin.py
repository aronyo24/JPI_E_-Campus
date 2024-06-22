from django.contrib import admin
from django.utils import timezone
from .models import Investment, Land, Staff


class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'quantity', 'other_info', 'log')
    list_filter = ('date', 'name')
    search_fields = ('date', 'quantity')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.submitted_by = request.user
            obj.log = f"{request.user.username}_{timezone.now()}"
        super().save_model(request, obj, form, change)


admin.site.register(Investment, InvestmentAdmin)


class LandAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'gher', 'mouza', 'dag_number', 'khatian_number', 'land_area', 'cultivable_land', 'adjacent_land',
        'owners_name', 'log')
    list_filter = ('date', 'gher')
    search_fields = ('date', 'khatian_number')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.submitted_by = request.user
            obj.log = f"{request.user.username}_{timezone.now()}"
        super().save_model(request, obj, form, change)


admin.site.register(Land, LandAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'name', 'post', 'salary', 'address', 'number', 'comments', 'log')
    list_filter = ('date', 'name')
    search_fields = ('date', 'salary')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.submitted_by = request.user
            obj.log = f"{request.user.username}_{timezone.now()}"
        super().save_model(request, obj, form, change)


admin.site.register(Staff, StaffAdmin)
