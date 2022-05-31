from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from deals.views import LandingPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('deals/', include('deals.urls', namespace="deals")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
