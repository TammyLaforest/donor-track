import django_filters

from django.db import models
from django.db.models import Q
from django.views import generic, View
from django.forms import inlineformset_factory
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

from contacts.filters import *
from contacts.tables import *
from contacts.models import *
from contacts.views import *
from contacts.views_auth import *


# inlineformset_factory creates a Class from a parent model (Contact)
# to a child model (Address)



def manage_vendor_form_set(request, Contact):
    Contact = Contact.objects.get(pk=uuid)
    contact_vendor_form_set = inlineformset_factory(
        Contact,
        Company_Vendor,
        Address,
        Email,
        Phone,
        fields = '__all__')
    if request.method == "POST":
        formset = contact_vendor_form_set(request.POST, request.FILES, instance=contact)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(contact.get_absolute_url())
    else:
        formset = contact_vendor_form_set(instance=contact)
    return render(request, 'vendors.html', {'formset': formset})

def manage_company_form_set(request, Contact):
    Contact = Contact.objects.get(pk=uuid)
    contact_company_form_set = inlineformset_factory(
        Contact,
        Company_Donor,
        Address,
        Email,
        Phone,
        fields = '__all__')
    if request.method == "POST":
        formset = contact_company_form_set(request.POST, request.FILES, instance=contact)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(contact.get_absolute_url())
    else:
        formset = contact_company_form_set(instance=contact)
    return render(request, 'donors.html', {'formset': formset})

def manage_individual_form_set(request, Contact):
    Contact = Contact.objects.get(pk=uuid)
    contact_individual_form_set = inlineformset_factory(
        Contact,
        Individual,
        Address,
        Email,
        Phone,
        fields = '__all__')
    if request.method == "POST":
        formset = contact_individual_form_set(request.POST, request.FILES, instance=contact)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(contact.get_absolute_url())
    else:
        formset = contact_individual_form_set(instance=contact)
    return render(request, 'donors.html', {'formset': formset})

def manage_couple_form_set(request, Contact):
    Contact = Contact.objects.get(pk=uuid)
    contact_couple_form_set = inlineformset_factory(
        Contact,
        Couple,
        Address,
        Email,
        Phone,
        fields = '__all__')
    if request.method == "POST":
        formset = contact_couple_form_set(request.POST, request.FILES, instance=contact)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(contact.get_absolute_url())
    else:
        formset = contact_couple_form_set(instance=contact)
    return render(request, 'donors.html', {'formset': formset})

def manage_other_form_set(request, Contact):
    Contact = Contact.objects.get(pk=uuid)
    contact_other_form_set = inlineformset_factory(
        Contact,
        Other,
        Address,
        Email,
        Phone,
        fields = '__all__')
    if request.method == "POST":
        formset = contact_other_form_set(request.POST, request.FILES, instance=contact)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(contact.get_absolute_url())
    else:
        formset = coontact_other_form_set(instance=contact)
    return render(request, 'donors.html', {'formset': formset})


# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'
#
# class DonorForm(ModelForm):
#     class Meta:
#         model = Donor
#         fields = '__all__'
#
# class VendorForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'


# class PartialAuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         exclude = ['title']

def contact_new(request):
    form = contact_other_form_set()
    return render(request, 'contacts/new_contact.html', {'form': form})


def donor_new(request):
    form = contact_couple_form_set()
    return render(request, 'contacts/new_donor.html', {'form': form})


def vendor_new(request):
    form = contact_vendor_form_set()
    return render(request, 'contacts/new_vendor.html', {'form': form})
