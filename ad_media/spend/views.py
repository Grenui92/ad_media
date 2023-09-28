from rest_framework.views import APIView
from rest_framework.response import Response

from .services import get_spend_by_name_date


class GetSpends(APIView):

    def get(self, request):
        """ 
        Eндпоинт в якому ми отримуємо
        queryset моделі SpendStatistic з поділом по дням (date) та назвою (name), з
        агрегованими сумами значень spend, impressions, clicks, conversion та
        пов'язаними значеннями revenue з моделі RevenueStatistic
        У body реквесту ви можете передати конкретну дату або ім'я. А можете не передавати. 

        return:
            Response: A JSON response containing data.
        Response format:
        {
            "result": grouped_revenue_spend
        }
        """

        date = request.data.get('date')
        name = request.data.get('name')

        result = get_spend_by_name_date(date=date, name=name)
        return Response({'result': result})
