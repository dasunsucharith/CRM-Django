from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Deal
from .forms import DealForm

# Create your views here.


def deal_list(request):

    deals = Deal.objects.all()
    context = {
        "deals": deals
    }

    return render(request, "deals/deal_list.html", context)


def deal_detail(request, pk):
    deal = Deal.objects.get(id=pk)
    context = {
        "deal": deal
    }

    return render(request, "deals/deal_detail.html", context)


def deal_create(request):
    context = {
        "form": DealForm()
    }
    return render(request, "deals/deal_create.html", context)
