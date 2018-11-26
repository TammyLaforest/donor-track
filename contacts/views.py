from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView

from contacts.models import Contact
from django.urls import reverse
from django.views.generic import CreateView


class ListContactView(ListView):

    model = Contact
    template_name = 'contacts.html'

class CreateContactView(CreateView):

    model = Contact
    template_name = 'edit_contact.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('contacts-list')

class IndexView(CreateView):

    model = Contact
    template_name = 'index.html'

    def get_success_url(self):
        return reverse('contacts-list')
