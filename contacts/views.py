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
from contacts.models import Contact, ContactForm, Select_ContactForm


class Select_ContactView(CreateView):
    model = Select_ContactForm
    template_name = 'contacts/detail.html'
    # category = Contact.objects.get(Category)
    # # {% for org in organisation %}
    #     #    <option value="{{org.id}}"
    #     #        {% if org == current_org %}selected="selected"{% endif %}>
    #     #        {{org.name|capfirst}}
    #     #    </option>
    #     # {% endfor %}
    #
    # if  category.lower() == donor:
    #     if Contact_Format.lower() == company:
    #         fields = ['Company', 'First_Name1', 'Last_Name1', 'Address_Number', 'Address_Street', 'Address_Street2', 'Address_City', 'Address_State', 'Address_Postal_Code', 'Address_Country', 'Phone1', 'Email1', 'Note']
    #     elif Contact_Format.lower() == individual:
    #         fields = ['First_Name1', 'Last_Name1', 'Address_Number', 'Address_Street', 'Address_Street2', 'Address_City', 'Address_State', 'Address_Postal_Code', 'Address_Country', 'Phone1', 'Email1', 'Note']
    #     elif Contact_Format.lower() == couple:
    #         fields = ['First_Name1', 'Last_Name1', 'First_Name2', 'Last_Name2','Address_Number', 'Address_Street', 'Address_Street2', 'Address_City', 'Address_State', 'Address_Postal_Code', 'Address_Country', 'Phone1', 'Email1', 'Phone2', 'Email2', 'Note']
    #     else:
    #         fields ='__all__'
    # if category.lower() == vendor:
    #     fields = ['Company', 'First_Name1', 'Last_Name1', 'Address_Number', 'Address_Street', 'Address_Street2', 'Address_City', 'Address_State', 'Address_Postal_Code', 'Address_Country', 'Phone1', 'Email1', 'Note']
    # else:
    #     fields ='__all__'




class ContactListView(ListView):
    model = Contact
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ContactsNameFilter(self.request.GET, queryset=self.get_queryset())
        return context

# class ContactDetailView(DetailView):
#     list_display = ['__all__']
#     model = Contact
#     template_name =

def ContactsTable(request):
    return render(request, 'contacts/detail.html', {'ContactsTable': Contact.objects.filter(Q(Owner=request.user))})


class contact_new_view(CreateView):
    model = Contact
    template_name = 'new_contact.html'
    fields = ('Company', 'First_Name1', 'Last_Name1', 'Address_Number',)
    #
    def get_success_url(self):
        return reverse('new_contact.html')

def contact_new(request):
    form = ContactForm()
    return render(request, 'contacts/new_contact.html', {'form': form})
