from contacts.models import Contact

from django.db import models
from django.db.models import Q
from django.views import generic, View
from django.views.generic import ListView, CreateView, DetailView, TemplateView
import django_filters
from django_filters.views import FilterView

from elasticsearch import Elasticsearch
from datetime import date
from haystack.generic_views import SearchView
from django import forms
from haystack.forms import SearchForm

class Thanks_View(CreateView):
    model = Contact
    template_name = 'thanks.html'
    fields = '__all__'

class DepositView(CreateView):

    model = Contact
    template_name = 'deposit.html'
    fields ='__all__'

class DonorDepositView(generic.ListView):
    model = Contact
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(DonorDepositView, self).get_context_data(**kwargs)
        # Need Paginator info
        context['object_list'] = Contact.objects.filter(Q(Contact_Category='donor')).order_by('Last_Name')
        return context


class DonorListDepositView(DetailView):
    model = Contact

    def get_deposit_data(self, **kwargs):
        context = super(DonorListDepositView, self).get_deposit_data(**kwargs)
        context['object_list'] = Contact.objects.filter(Q(Contact_Category='donor')).order_by('Last_Name')
        return context
