from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subadmin/', views.subadmin, name='subadmin'),

    path('subadmin/fishbuy/', views.fishbuy, name='fishbuy'),  # Add forward slash
    path('subadmin/dailycost/', views.dailycost, name='dailycost'),  # Add forward slash
    path('subadmin/salary/', views.salary, name='salary'),  # Add forward slash
    path('subadmin/investment/', views.investments, name='investments'),  # Add forward slash
    path('subadmin/land/', views.land, name='land'),  # Add forward slash
    path('subadmin/staff/', views.staff, name='staff'),  # Add forward slash
    path('subadmin/earnings/', views.earnings, name='earnings'),  # Add forward slash
    path('subadmin/monthly_report/', views.monthly_report, name='monthly_report')  # Add forward slash
]
