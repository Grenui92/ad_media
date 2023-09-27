from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from random import random
from django.db.models import Sum

from spend.models import SpendStatistic
from .models import RevenueStatistic
from .serealizers import RevenueStatisticSerializer


class CreateDB(APIView):
    
    def post(self, request):
        print(request)
        for k in range(1, 10):
            SpendStatistic.objects.create(
                name = f'{k}',
                date = f'2023-06-0{k}',
                spend = k + 0.28,
                impressions = k*2,
                clicks = k*1000,
                conversion = k*100
            )
            
            SpendStatistic.objects.create(
                name = f'{k}s',
                date = f'2023-06-0{k}',
                spend = k + 0.4,
                impressions = k*2,
                clicks = k*1000+1,
                conversion = k*100+1
            )
        for k in range(1, 10):
            RevenueStatistic.objects.create(
                name=f'{k}',
                spend = SpendStatistic.objects.get(name=f'{k}'),
                date = f'2023-06-0{k}',
                revenue = k*50
            )
            RevenueStatistic.objects.create(
                name=f'{k}',
                spend = SpendStatistic.objects.get(name=f'{k}s'),
                date = f'2023-06-0{k}',
                revenue = k*55
            )

class GetRevenue(APIView):

    def get(self, request):
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
        return Response({'result':result})