from django.urls import path
from .views import deal_list
from .views import deal_detail
from .views import deal_create
from .views import deal_update
from .views import deal_delete

app_name = "deals"

urlpatterns = [
    path('', deal_list, name='deal-list'),
    path('create/', deal_create, name='deal-create'),
    path('<int:pk>/', deal_detail, name='deal-detail'),
    path('<int:pk>/update/', deal_update, name='deal-update'),
    path('<int:pk>/delete/',deal_delete, name='deal-delete'),
]
