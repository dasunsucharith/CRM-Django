from django.urls import path
from .views import DealListView, DealDetailView, DealCreateView, DealUpdateView, DealDeleteView

app_name = "deals"

urlpatterns = [
    path('', DealListView.as_view(), name='deal-list'),
    path('create/', DealCreateView.as_view(), name='deal-create'),
    path('<int:pk>/', DealDetailView.as_view(), name='deal-detail'),
    path('<int:pk>/update/', DealUpdateView.as_view(), name='deal-update'),
    path('<int:pk>/delete/', DealDeleteView.as_view(), name='deal-delete'),
]
