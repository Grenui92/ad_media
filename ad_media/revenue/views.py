from rest_framework.response import Response
from rest_framework.views import APIView

from .services import get_revenue_by_date_name


class GetRevenue(APIView):

    def get(self, request, date=None, name=None):
        """ 
        Ендпоинт в якому ми отримуємо
        queryset моделі RevenueStatistic з поділом по дням (date) та назвою (name), з
        агрегованими сумами значень revenue та пов'язаними значеннями spend,
        impressions, clicks, conversion з моделі SpendStatistic. 
        У body реквесту ви можете передати конкретну дату або ім'я. А можете не передавати. 

        return:
            Response: A JSON response containing data.
        Response format:
        {
            "result": grouped_revenue_spend
        }
        """

        grouped_revenue_spend = get_revenue_by_date_name(date=date, name=name)

        return Response({'result': grouped_revenue_spend})
