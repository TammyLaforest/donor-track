import django_filters


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
from contacts.models import Contact, ContactForm

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


class contact_new_view(CreateView):
    model = Contact
    template_name = 'new_contact.html'
    fields = '__all__'
    #
    def get_success_url(self):
        return reverse('new_contact.html')

def contact_new(request):
    form = ContactForm()
    return render(request, 'contacts/new_contact.html', {'form': form})
