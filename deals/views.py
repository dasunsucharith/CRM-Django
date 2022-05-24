from multiprocessing import context
from django.shortcuts import render
from .models import Deal

# Create your views here.


def home_page(request):

    deals = Deal.objects.all()
    context = {
        "deals": deals
    }

    return render(request, "home_page.html", context)
