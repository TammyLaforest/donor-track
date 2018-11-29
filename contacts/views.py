import django_filters
import django_tables2 as tables
from django_tables2.views import SingleTableMixin

from django.db import models
from django.db.models import Q
from django.views import generic, View
from django.views.generic import ListView, CreateView, DetailView, TemplateView

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
# from django.contrib import auth
# from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .filters import ContactsNameFilter
from .models import Contact

class ContactListView(ListView):
    model = Contact
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ContactsNameFilter(self.request.GET, queryset=self.get_queryset())
        return context

class ContactDetailView(DetailView):
    list_display = ['__all__']
    model = Contact
    template_name = 'contacts/detail.html'

def ContactsTable(request):
    return render(request, 'contacts/detail.html', {'ContactsTable': Contact.objects.filter(Q(Owner=request.user))})


class ContactContactView(CreateView):
    model = Contact
    template_name = 'new.html'
    fields = '__all__'
    #
    def get_success_url(self):
        return reverse('contacts.html')

def donortable(request):
    table = DonorTableMaker(Contact.objects.all())
    return render(request, 'donors.html', {'donortable': Contact.objects.filter(Q(Category='regular') | Q(Category='member') | Q(Category='first_time') | Q(Category='Annual') | Q(Category='grant') | Q(Category='otherdonor'))})
