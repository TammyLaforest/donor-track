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
from contacts.forms import *
from contacts.models import *
from contacts.tables import *
# from contacts.views import *
from contacts.views_auth import *


class all_categories_view(CreateView):
    model = Category
    template_name = 'contacts/contacts.html'

# class subcategories_view(CreateView):
#     model = Subcategory
#     template_name = 'contacts/contacts.html'
#

class contacts_view(LoggedInMixin, ContactOwnerMixin, DetailView):
    model = Contact
    template_name = 'contacts/contacts.html'
    fields = '__all__'

class donors_view(LoggedInMixin, ContactOwnerMixin, DetailView):
    model = Contact
    template_name = 'contacts/donors.html'
    fields = '__all__'

class contact_new_view(CreateView):
    form_class= generic_contact_form
    Owner = User
    template_name = 'contacts/new_contact_generic.html'

    def get_success_url(self):
        return reverse('contacts/new_contact_generic.html')

class new_donor_individual_view(CreateView):
    form_class= new_donor_individual_form
    model = Contact
    Owner=User
    Account = 'Last_Name'+'', ''+ 'First_Name'
    template_name = 'contacts/new_donor_individual.html'
    #
    def get_success_url(self):
        return reverse('contacts/new_donor_individual.html')

class new_donor_couple_view(CreateView):
    form_class= new_donor_couple_form
    model = Contact
    Owner=User
    template_name = 'contacts/new_donor_couple.html'
    #
    def get_success_url(self):
        return reverse('contacts/new_donor_couple.html')

class new_donor_business_view(CreateView):
    form_class= new_donor_business_form
    model = Contact
    Owner=User
    template_name = 'contacts/new_donor_business.html'
    #
    def get_success_url(self):
        return reverse('contacts/new_donor_business.html')


# def donor_new(request):
#     form = DonorForm()
#     return render(request, 'contacts/new_donor.html', {'form': form})

class donor_categories_view(LoggedInMixin, ContactOwnerMixin, DetailView):
    model = Contact
    template_name = 'contacts/donor_categories.html'
    fields = '__all__'



# Vendors Section

class vendors_view( LoggedInMixin, ContactOwnerMixin, DetailView):
    model = Contact
    template_name = 'contacts/vendors.html'
    fields = '__all__'


class new_vendor_view(CreateView):
    model = Contact
    template_name = 'contacts/new_vendor.html'
    fields = '__all__'
    #
    def get_success_url(self):
        return reverse('contacts/vendors.html')

def vendor_new(request):
    form = business_vendor_contact_form()
    return render(request, 'contacts/new_vendor.html', {'form': form})


# class new_vendor_view(LoggedInMixin, ContactOwnerMixin, DetailView):
#     form_class = business_vendor_contact_form()
#     model = Contact
#     Owner=User
#     exclude = ['First_Name2', 'Last_Name2', 'Email2', 'Owner']
#     success_url = reverse_lazy('vendors')
#     template_name = 'new_vendor.html'

# class vendor_new_view(CreateView):
#     model = Contact
#     template_name = 'contacts/new_vendor.html'
#     fields = '__all__'
#
#     def get_success_url(self):
#         return reverse('contacts/new_vendor.html')

# def vendor_new(request):
#     form = VendorForm()
#     return render(request, 'contacts/new_vendor.html', {'form': form})

class vendor_categories_view(CreateView):
    model = Contact
    template_name = 'contacts/vendor_categories.html'
    fields = '__all__'
