from django.shortcuts import render

from contacts.models import Contact

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views import generic
from django.views.generic import ListView, CreateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Contact

class ListContactView(ListView):

    list_display = ['__all__']
    model = Contact
    template_name = 'contacts.html'

class CreateContactView(CreateView):

    model = Contact
    template_name = 'new.html'
    fields = '__all__'
    #
    def get_success_url(self):
        return reverse('contacts.html')

def contactstable(request):
    return render(request, 'contacts/contacts.html', {'contactstable': Contact.objects.all()})

def donortable(request):
    return render(request, 'donors/donors.html', {'donortable': Contacts.objects.filter()})
