from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Deal, Agent
from .forms import DealForm, DealModelForm

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
    form = DealModelForm()
    if request.method == "POST":
        print('Receiving a post request')
        form = DealModelForm(request.POST)
        if form.is_valid():
            print('The form is valid')
            print(form.cleaned_data)
            contact_person = form.cleaned_data['contact_person']
            organization = form.cleaned_data['organization']
            title = form.cleaned_data['title']
            value = form.cleaned_data['value']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            agent = Agent.objects.first()
            Deal.objects.create(
                contact_person=contact_person,
                organization=organization,
                title=title,
                value= value,
                phone=phone,
                email=email,
                agent=agent,
            )
            print('The deal has been created!')
            return redirect('/deals')
    context = {
        "form": form
    }
    return render(request, "deals/deal_create.html", context)
