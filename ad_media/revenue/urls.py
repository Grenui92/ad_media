from django.urls import path
from .views import GetRevenue

urlpatterns = [
    path('get_all_revenues/', GetRevenue.as_view(), name='get_revenues')
]
