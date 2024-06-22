from django.db import models
from django.contrib.auth.models import User


class LoginLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=100)
    site_name = models.CharField(max_length=100, default='Default Site Name')  # Add default value for site_name

    def __str__(self):
        return f"{self.user.username} - {self.login_time} - {self.ip_address} - {self.site_name}"


class datasave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.date} - {self.date}"