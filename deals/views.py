from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.views import generic
from .models import Deal, Agent
from .forms import DealForm, DealModelForm, CustomUserCreationForm

# Create your views here.


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


""" def landing_page(request):
    return render(request, "landing.html") """


class DealListView(generic.ListView):
    template_name = "deals/deal_list.html"
    queryset = Deal.objects.all()
    context_object_name = "deals"


""" def deal_list(request):

    deals = Deal.objects.all()
    context = {
        "deals": deals
    }

    return render(request, "deals/deal_list.html", context) """


class DealDetailView(generic.DetailView):
    template_name = "deals/deal_detail.html"
    queryset = Deal.objects.all()
    context_object_name = "deal"


""" def deal_detail(request, pk):
    deal = Deal.objects.get(id=pk)
    context = {
        "deal": deal
    }

    return render(request, "deals/deal_detail.html", context) """


class DealCreateView(generic.CreateView):
    template_name = "deals/deal_create.html"
    form_class = DealModelForm

    def get_success_url(self):
        return reverse("deals:deal-list")

    def form_valid(self, form):
        send_mail(
            subject="A Deal has been created",
            message="Go to the site to see the new deal",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(DealCreateView, self).form_valid(form)


""" def deal_create(request):
    form = DealModelForm()
    if request.method == "POST":
        print('Receiving a post request')
        form = DealModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/deals')
    context = {
        "form": form
    }
    return render(request, "deals/deal_create.html", context)
 """


class DealUpdateView(generic.UpdateView):
    template_name = "deals/deal_update.html"
    queryset = Deal.objects.all()
    form_class = DealModelForm

    def get_success_url(self):
        return reverse("deals:deal-list")


""" def deal_update(request, pk):
    deal = Deal.objects.get(id=pk)
    form = DealModelForm(instance=deal)
    if request.method == "POST":
        form = DealModelForm(request.POST, instance=deal)
        if form.is_valid():
            form.save()
            return redirect("/deals")
    context = {
        "form": form,
        "deal": deal
    }
    return render(request, "deals/deal_update.html", context) """


class DealDeleteView(generic.DeleteView):
    template_name = "deals/deal_delete.html"
    queryset = Deal.objects.all()

    def get_success_url(self):
        return reverse("deals:deal-list")


""" def deal_delete(request, pk):
    deal = Deal.objects.get(id=pk)
    deal.delete()
    return redirect("/deals")
 """

""" def deal_update(request, pk):
    deal = Deal.objects.get(id=pk)
    form = DealForm()
    if request.method == "POST":
        print('Receiving a post request')
        form = DealForm(request.POST)
        if form.is_valid():
            print('The form is valid')
            print(form.cleaned_data)
            contact_person = form.cleaned_data['contact_person']
            organization = form.cleaned_data['organization']
            title = form.cleaned_data['title']
            value = form.cleaned_data['value']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            deal.contact_person = contact_person
            deal.organization = organization
            deal.title = title
            deal.value = value
            deal.phone = phone
            deal.email = email
            deal.save()
            return redirect('/deals')
    context = {
        "form": form,
        "deal": deal
    }
    return render(request, "deals/deal_update.html", context) """


""" def deal_create(request):
    form = DealForm()
    if request.method == "POST":
        print('Receiving a post request')
        form = DealForm(request.POST)
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
    return render(request, "deals/deal_create.html", context) """
