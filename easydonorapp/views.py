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

# class MySearchForm(SearchForm):
#     # model = Contact
#     searchbar = forms.CharField(required=True)
#     def search(self):
#         # First, store the SearchQuerySet received from other processing.
#         sqs = super(MySearchForm, self).search()
#         if not self.is_valid():
#             return self.no_query_found()
#
#         if self.cleaned_data['searchbar']:
#             sqs = sqs.filter(First_Name__Contact=self.cleaned_data['searchbar'])
#
#         return sqs
#
#
#
# class MySearchView(SearchView):
#     # model = Contact
#     def get_queryset(self):
#         queryset = super(MySearchView, self).get_queryset()
#         # further filter queryset based on some set of criteria
#         return queryset.filter(pub_date__gte=date(2015, 1, 1))
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(MySearchView, self).get_context_data(*args, **kwargs)
#         # do something
#         return context
