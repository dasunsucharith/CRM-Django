from django.urls import path
from .views import deal_list
from .views import deal_detail
from .views import deal_create
from .views import deal_update

app_name = "deals"

urlpatterns = [
    path('', deal_list),
    path('create/', deal_create),
    path('<int:pk>/', deal_detail),
    path('<int:pk>/update/', deal_update)
]
