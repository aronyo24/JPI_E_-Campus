from django.db.models import Sum
from cost.models import FishPurchase, DailyCost


def get_fish_data():
    fish_data = FishPurchase.objects.values('fish_name').annotate(total_quantity=Sum('quantity'),
                                                                  total_price=Sum('price'))
    return fish_data


def get_daily_cost():
    daily_cost = DailyCost.objects.values('expenditure_sector').annotate(total_cost_amount=Sum('cost_amount'))
    return daily_cost
