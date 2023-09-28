from django.db.models import Sum, Q

from .models import RevenueStatistic


def get_revenue_by_date_name(date, name):
    """
    The get_spend_by_name_date function takes in a date and name, and returns the total spend, impressions, clicks, conversions
    and revenue for that date/name combination. If no parameters are passed in it will return all of the data.

    :param date: Filter the results by date
    :param name: Filter the results by name
    :return: A queryset of dictionaries
    """
    
    result = (
        RevenueStatistic.objects
        .values('date', 'name')
        .annotate(
            total_revenue=Sum('revenue'),
            total_spend=Sum('spend__spend'),
            total_impressions=Sum('spend__impressions'),
            total_clicks=Sum('spend__clicks'),
            total_conversion=Sum('spend__conversion')
        )
    )
    if date or name:
        result = result.filter(Q(name=name) | Q(date=date))
    return result
