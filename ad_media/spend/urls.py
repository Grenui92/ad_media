from django.urls import path

from .views import GetSpends
urlpatterns = [
    path('get_all_spending/', GetSpends.as_view(), name='get_all_spending')
]
