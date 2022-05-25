from multiprocessing import context
from django.shortcuts import render
from .models import Deal

# Create your views here.


def deal_list(request):

    deals = Deal.objects.all()
    context = {
        "deals": deals
    }

    return render(request, "deals/deal_list.html", context)
