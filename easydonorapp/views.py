from django.db import models
from django.conf import settings
from django.db.models import Q
from django.views import generic, View
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django import forms
from django.forms import ModelForm
from contacts.models import Contact
from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import redirect
from django.urls import reverse

from contacts.models import Contact
from users.models import Profile

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_contacts = Contact.objects.all().count()
    num_instances = ContactInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = ContactInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_profiles = Profile.objects.count()

    context = {
        'num_contacts': num_contacts,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_profiles': num_profiles,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

















def my_view(request):
    ...
    obj = MyModel.objects.get(...)
    return redirect(obj, permanent=True)


# pages/views.py
class HomePageView(TemplateView):
    template_name = 'home.html'

class Thanks_View(CreateView):
    model = Contact
    template_name = 'thanks.html'
    fields = '__all__'

class DepositView(CreateView):

    model = Contact
    template_name = 'deposit.html'
    fields ='__all__'

class DonorListDepositView(ListView):

    model = Contact
    template_name = 'deposit.html'
    fields ='__all__'

class DonorDepositView(CreateView):

    model = Contact
    template_name = 'deposit.html'
    fields ='__all__'
