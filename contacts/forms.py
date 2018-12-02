import django_filters

from django.db import models
from django.db.models import Q
from django.views import generic, View
from django.forms import inlineformset_factory, formset_factory, BaseInlineFormSet, ModelForm
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset


from contacts.filters import *
from contacts.tables import *
from contacts.models import *
from contacts.views import *
from contacts.views_auth import *

class generic_contact_form(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class new_donor_individual_form(ModelForm):
    class Meta:
        model = Contact
        Owner=User
        Contact_Format = 'Individual'
        Account = 'Last_Name'+'', ''+ 'First_Name'
        fields = '__all__'
        exclude =['First_Name2', 'Last_Name2', 'Phone2', 'Email2', 'Company', 'Owner', 'Category', 'Vendor_Subcategory', 'Contact_Format' ]

class new_donor_couple_form(ModelForm):
    class Meta:
        model = Contact
        Owner=User
        Contact_Format = 'Couple'
        Account = 'Last_Name'+'', ''+ 'First_Name' + '&' + 'Last_Name2'+'', ''+ 'First_Name2'
        fields = '__all__'
        exclude =[ 'Company', 'Owner', 'Category', 'Vendor_Subcategory', 'Contact_Format' ]

# 
# class new_donor_business_form(ModelForm):
#     class Meta:
#         model = Contact
#         Owner=User
#         Contact_Format = 'Business'
#         Account = 'Company'
#         fields = '__all__'
#         exclude =['First_Name2', 'Last_Name2', 'Phone2', 'Email2', 'Owner', 'Category', 'Vendor_Subcategory', 'Contact_Format' ]
#
#
# class business_vendor_contact_form(ModelForm):
#     class Meta:
#         model = Contact
#         Owner=User
#         exclude = ['First_Name2', 'Last_Name2', 'Email2', 'Owner']
#
# # LoggedInMixin, ContactOwnerMixin, DetailView
