from django.db.models import Sum, Q

from .models import SpendStatistic


def get_spend_by_name_date(date, name):
    """
    The get_spend_by_name_date function takes in a date and name, and returns the total spend, impressions, clicks, conversions
    and revenue for that date/name combination. If no parameters are passed in it will return all of the data.

    :param date: Filter the results by date
    :param name: Filter the results by name
    :return: A queryset of dictionaries
    """

    result = (
        SpendStatistic.objects.values('date', 'name')
        .annotate(
            total_spend=Sum('spend'),
            total_impressions=Sum('impressions'),
            total_clicks=Sum('clicks'),
            total_conversion=Sum('conversion'),
            total_revenue=Sum('revenuestatistic__revenue')
        )
    )
    if date or name:
        result = result.filter(Q(name=name) | Q(date=date))
    return result
