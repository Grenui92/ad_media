from django.urls import path
from .views import GetRevenue, CreateDB
urlpatterns = [
    path('create_db/', CreateDB.as_view(), name='create_db'),
    path('get_all/', GetRevenue.as_view(), name='get_revenue')
]
