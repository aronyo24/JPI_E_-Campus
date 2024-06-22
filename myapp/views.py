from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone
from django.db.models import Sum

from cost.models import FishPurchase, DailyCost
from myapp.models import LoginLog
from cost.forms import FishPurchaseForm, DailyCostForm, SalaryForm
from earning.forms import EarningForm
from investment.forms import InvestmentForm, LandForm, StaffForm
from .get_data import get_fish_data


@login_required(login_url='/login/')
def subadmin(request):
    username = request.user.username
    return render(request, 'index.html', {'username': username})


@login_required(login_url='/login/')
def fishbuy(request):
    username = request.user.username
    if request.method == 'POST':
        form = FishPurchaseForm(request.POST)
        if form.is_valid():
            form.instance.log = f"{request.user.username} at {timezone.now()}"
            form.save()
            messages.success(request, 'Fish purchase information saved successfully!')
            return redirect('fishbuy')
        else:
            messages.error(request, 'Error saving fish purchase information!')
    else:
        form = FishPurchaseForm()
    return render(request, 'fishbuy.html', {'form': form, 'username': username})


@login_required(login_url='/login/')
def dailycost(request):
    username = request.user.username
    if request.method == 'POST':
        form = DailyCostForm(request.POST)
        if form.is_valid():
            form.instance.log = f"{request.user.username} at {timezone.now()}"
            form.save()
            messages.success(request, 'Daily Cost information saved successfully!')
            return redirect('dailycost')
        else:
            messages.error(request, 'Error saving Daily Cost information!')
    else:
        form = DailyCostForm()
    return render(request, 'dailycost.html', {'form': form, 'username': username})


@login_required(login_url='/login/')
def salary(request):
    username = request.user.username
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.instance.log = f"{request.user.username} at {timezone.now()}"
            form.save()
            messages.success(request, 'Salary information saved successfully!')
            return redirect('salary')
        else:
            messages.error(request, 'Error saving Salary information')
    else:
        form = SalaryForm()
    return render(request, 'salary.html', {'form': form, 'username': username})


@login_required(login_url='/login/')
def earnings(request):
    username = request.user.username
    if request.method == 'POST':
        form = EarningForm(request.POST)
        if form.is_valid():
            form.instance.log = f"{request.user.username} at {timezone.now()}"
            form.save()
            messages.success(request, "Earning information saved successfully!")
            return redirect('earnings')
        else:
            messages.error(request, "Error saving Earning information")
    else:
        form = EarningForm()
    return render(request, 'earnings.html', {'form': form, 'username': username})


@login_required(login_url='/login/')
def investments(request):
    username = request.user.username
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            form.instance.log = f"{request.user.username} at {timezone.now()}"
            form.save()
            messages.success(request, "Investment information saved successfully!")
            return redirect('investments')
        else:
            messages.error(request, "Error saving Investment information")
    else:
        form = InvestmentForm()
    return render(request, 'investment.html', {'form': form, 'username': username})


@login_required(login_url='/login/')
def land(request):
    username = request.user.username
    if request.method == 'POST':
        form = LandForm(request.POST)
        if form.is_valid():
            form.instance.log = f"{request.user.username} at {timezone.now()}"
            form.save()
            messages.success(request, "Land information saved successfully!")
            return redirect("land")
        else:
            messages.error(request, "Error saving Land information")
    else:
        form = LandForm()
    return render(request, 'land.html', {'form': form, 'username': username})


@login_required(login_url='/login/')
def staff(request):
    username = request.user.username
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.instance.log = f"{request.user.username} at {timezone.now()}"
            form.save()
            messages.success(request, "Staff information saved successfully!")
            return redirect("staff")
        else:
            messages.error(request, "Error saving Staff information")
    else:
        form = StaffForm()
    return render(request, 'staff.html', {'form': form, 'username': username})


@receiver(user_logged_in)
def user_logged_in_receiver(sender, user, request, **kwargs):
    site_name = request.get_host() + request.path
    LoginLog.objects.create(user=user, ip_address=request.META.get('REMOTE_ADDR'), site_name=site_name)

@login_required(login_url='/login/')
def monthly_report(request):
    if request.method == 'GET':
        month = request.GET.get('month')
        year = request.GET.get('year')

        if month and year:
            try:
                month = int(month)
                year = int(year)

                start_date = datetime(year, month, 1)
                end_date = datetime(year, month, 1).replace(day=1, month=month + 1) - timedelta(days=1)

                fish_data = FishPurchase.objects.filter(date__range=[start_date, end_date]).values(
                    'fish_name').annotate(
                    total_quantity=Sum('quantity'), total_price=Sum('price'))
                cost_data = DailyCost.objects.filter(date__range=[start_date, end_date]).values(
                    'expenditure_sector').annotate(
                    total_cost_amount=Sum('cost_amount'))

                total_quantity_all = FishPurchase.objects.filter(date__range=[start_date, end_date]).aggregate(
                    Sum('quantity'))
                total_price_all = FishPurchase.objects.filter(date__range=[start_date, end_date]).aggregate(
                    Sum('price'))

                total_cost_amount_all = DailyCost.objects.filter(date__range=[start_date, end_date]).aggregate(
                    Sum('cost_amount'))

                context = {
                    'fish_data': fish_data,
                    'total_quantity_all': total_quantity_all,
                    'total_price_all': total_price_all,
                    'cost_data': cost_data,
                    'total_cost_amount_all': total_cost_amount_all
                }
                return render(request, 'monthly_report.html', context)
            except ValueError:
                messages.error(request, 'Invalid month or year!')
        else:
            messages.error(request, 'Both month and year are required!')
            return render(request, 'monthly_report.html', )

    return redirect('monthly_report')
