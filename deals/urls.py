from django.urls import path
from .views import deal_list
from .views import deal_detail
from .views import deal_create

app_name = "deals"

urlpatterns = [
    path('', deal_list),
    path('create/', deal_create),
    path('<pk>/', deal_detail)
]
