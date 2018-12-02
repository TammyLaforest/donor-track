import django_filters

from django.db import models
from django.db.models import Q
from django.views import generic, View
from django.views.generic import ListView, CreateView, DetailView, TemplateView

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.contrib.auth.models import User

from contacts.filters import *
# from contacts.forms import *
from contacts.models import *
from contacts.tables import *
# from contacts.views import *
from contacts.views_auth import *

# class ListContactView(LoggedInMixin, ListView):
#
#     model = Contact
#     template_name = 'contact_list.html'
#
#     def get_queryset(self):
#
#         return Contact.objects.filter(owner=self.request.user)
# from django.core.exceptions import PermissionDenied
# ...



class all_categories_view(CreateView):
    model = Category
    template_name = 'contacts/contacts.html'

class subcategories_view(CreateView):
    model = Subcategory
    template_name = 'contacts/contacts.html'



class contacts_view(LoggedInMixin, ContactOwnerMixin, DetailView):
    model = Contact
    template_name = 'contacts/contacts.html'


class contact_new_view(CreateView):
    model = Contact
    template_name = 'contacts/new_contact.html'
    fields = '__all__'
    #
    def get_success_url(self):
        return reverse('contacts/new_contact.html')

def contact_new(request):
    form = ContactForm()
    return render(request, 'contacts/new_contact.html', {'form': form})


# Donors Section

class donors_view(LoggedInMixin, ContactOwnerMixin, DetailView):
    model = Contact
    template_name = 'contacts/donors.html'
    fields = '__all__'


class donor_new_view(CreateView):
    model = Contact
    template_name = 'contacts/new_donor.html'
    fields = ['First_Name1', 'Last_Name1', 'First_Name2', 'Last_Name2', ]
    #
    def get_success_url(self):
        return reverse('contacts/new_donor.html')

def donor_new(request):
    form = DonorForm()
    return render(request, 'contacts/new_donor.html', {'form': form})

class donor_categories_view(LoggedInMixin, ContactOwnerMixin, DetailView):
    model = Contact
    template_name = 'contacts/donor_categories.html'
    fields = '__all__'



# Vendors Section

class vendors_view(LoggedInMixin, ContactOwnerMixin, DetailView):
    model = Contact
    template_name = 'contacts/vendors.html'
    fields = '__all__'


class vendor_new_view(CreateView):
    model = Contact
    template_name = 'contacts/new_vendor.html'
    fields = ['First_Name1', 'Last_Name1', 'Company' ]
    #
    def get_success_url(self):
        return reverse('contacts/new_vendor.html')

def vendor_new(request):
    form = VendorForm()
    return render(request, 'contacts/new_vendor.html', {'form': form})

class vendor_categories_view(CreateView):
    model = Contact
    template_name = 'contacts/vendor_categories.html'
    fields = '__all__'
