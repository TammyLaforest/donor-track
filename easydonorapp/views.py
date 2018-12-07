from django.db import models
from django.conf import settings
from django.db.models import Q
from django.views import generic, View
from django.views.generic import ListView, CreateView, DetailView, TemplateView, FormView
from django import forms
from django.forms import ModelForm
from contacts.models import Contact
from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import redirect
from django.urls import reverse

from contacts.models import Contact
from users.models import Profile

# def index(request):
#     """View function for home page of site."""
#
#     # Generate counts of some of the main objects
#     num_contacts = Contact.objects.all().count()
#     num_instances = ContactInstance.objects.all().count()
#
#     # Available books (status = 'a')
#     num_instances_available = ContactInstance.objects.filter(status__exact='a').count()
#
#     # The 'all()' is implied by default.
#     num_profiles = Profile.objects.count()
#
#     context = {
#         'num_contacts': num_contacts,
#         'num_instances': num_instances,
#         'num_instances_available': num_instances_available,
#         'num_profiles': num_profiles,
#     }
#
#     # Render the HTML template index.html with the data in the context variable
#     return render(request, 'index.html', context=context)



# Understand instances in order to associate pledges with donor profiles.

class HomePageView(TemplateView):
    template_name = 'home.html'

class ErrorView(TemplateView):
    template_name = 'nope.html'

class ThanksView(CreateView):
    model = Contact
    template_name = 'thanks.html'
    fields = '__all__'

class DepositDetailView(ListView):

    model = Contact
    template_name = 'deposit-detail.html'
    fields ='__all__'

class DepositListView(ListView):

    model = Contact
    template_name = 'deposit-list.html'
    fields ='__all__'

class DepositView(FormView):

    model = Contact
    template_name = 'deposit.html'
    fields ='__all__'

def get_deposit(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DepositForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/home/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DepositForm()

    return render(request, 'deposit.html', {'form': form})
