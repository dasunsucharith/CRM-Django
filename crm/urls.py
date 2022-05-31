from django.contrib import admin
from django.urls import path, include
from deals.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('deals/', include('deals.urls', namespace="deals"))
]
