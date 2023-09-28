from decimal import Decimal, ROUND_HALF_UP

from rest_framework.test import APITestCase, RequestsClient, APIClient

from .models import RevenueStatistic
from spend.models import SpendStatistic

class SpendTest(APITestCase):
    
    def setUp(self) -> None:
        """
        The setUp function creates four SpendStatistic objects and four RevenueStatistic objects.
        The first two SpendStatistic nad RevenueStatistic objects have the same date, while the second two have a different date.
        All SpendStatistic and RevenueStaticstic objects have the same name.
        The first two RevenueStatistic objects are linked to the first set of SpendStatistics, while 
        the second set of RevenueStatistics are linked to the second set of SpendStatistics.
        """
        
        self.spend1 = SpendStatistic.objects.create(name='1',
                                                    date='2023-06-01',
                                                    spend=Decimal(100.55),
                                                    impressions=100,
                                                    clicks=50,
                                                    conversion=100/50)
        self.spend2 = SpendStatistic.objects.create(name='1',
                                                    date='2023-06-01',
                                                    spend=Decimal(200.55),
                                                    impressions=200,
                                                    clicks=60,
                                                    conversion=200/50)
        self.spend3 = SpendStatistic.objects.create(name='1',
                                                    date='2023-06-02',
                                                    spend=Decimal(300.55),
                                                    impressions=300,
                                                    clicks=70,
                                                    conversion=300/50)
        self.spend4 = SpendStatistic.objects.create(name='1',
                                                    date='2023-06-02',
                                                    spend=Decimal(400.55),
                                                    impressions=400,
                                                    clicks=80,
                                                    conversion=400/50)
        
        self.revenue1 = RevenueStatistic.objects.create(name='1',
                                                        date='2023-06-01',
                                                        spend=self.spend1,
                                                        revenue=Decimal(500))
        self.revenue2 = RevenueStatistic.objects.create(name='1',
                                                        date='2023-06-01',
                                                        spend=self.spend2,
                                                        revenue=Decimal(600))
        self.revenue3 = RevenueStatistic.objects.create(name='1',
                                                        date='2023-06-02',
                                                        spend=self.spend3,
                                                        revenue=Decimal(700))
        self.revenue4 = RevenueStatistic.objects.create(name='1',
                                                        date='2023-06-02',
                                                        spend=self.spend4,
                                                        revenue=Decimal(800))
        self.revenue5 = RevenueStatistic.objects.create(name='1',
                                                        date='2023-06-03',
                                                        spend=None,
                                                        revenue=Decimal(800))
        self.revenue6 = RevenueStatistic.objects.create(name='1',
                                                        date='2023-06-03',
                                                        spend=None,
                                                        revenue=Decimal(800))
    
    def test_1(self):
        """
        The test_1 function tests the get_all_revenues API endpoint.
        It first creates a client to make requests to the server, then makes a request for all spending data.
        The test then checks that the total spend and revenue are correct.
        """
        client = APIClient()
        result = client.get('http://127.0.0.1:8000/api/v1/revenue/get_all_revenues/')

        target = result.data['result'][0]
        
        expected_spend = (self.spend1.spend+self.spend2.spend).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        self.assertEqual(target['total_spend'], expected_spend)
        
        expected_revenue = (self.revenue1.revenue+self.revenue2.revenue).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        self.assertEqual(target['total_revenue'], expected_revenue)
        
    def test_with_spend_None(self):
        """
        The test_with_spend_None function tests the case where there is no spend data.
        The expected result is that the total_spend field should be None, and the total_revenue field should be equal to 
        the sum of revenue5 and revenue6.
        """
        
        client = APIClient()
        result = client.get('http://127.0.0.1:8000/api/v1/revenue/get_all_revenues/')
        target = result.data['result'][1]

        expected_spend = None
        self.assertEqual(target['total_spend'], expected_spend)
        
        expected_revenue = (self.revenue5.revenue+self.revenue6.revenue).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        self.assertEqual(target['total_revenue'], expected_revenue)