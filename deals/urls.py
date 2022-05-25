from django.urls import path 
from .views import deal_list

app_name = "deals" 

urlpatterns = [
    path('', deal_list)
]
