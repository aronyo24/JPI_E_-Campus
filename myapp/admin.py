from django.contrib import admin
from .models import LoginLog


class LoginLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'login_time', 'ip_address', 'site_name')  # Fields to display in the list view


admin.site.register(LoginLog, LoginLogAdmin)
