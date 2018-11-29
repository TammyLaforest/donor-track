from django.db import models
from django.db.models import Q
from .models import Contact, Person

import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views import generic
from django.views.generic import ListView, CreateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required




class ListContactView(ListView):

    list_display = ['__all__']
    model = Contact
    template_name = 'contacts.html'

@login_required
def contactstable(request):
    return render(request, 'contacts/contacts.html', {'contactstable': Contact.objects.all()})

# 
# def people(request):
#     return render(request, 'contacts/contacts.html', {'people': Person.objects.all()})

class CreateContactView(CreateView):

    model = Contact
    template_name = 'new.html'
    fields = '__all__'
    #
    def get_success_url(self):
        return reverse('contacts.html')


class CoupleFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ['Last_Name1', 'First_Name1', 'Last_Name2', 'First_Name2', 'Category']


@permission_required('contacts', login_url="/login/")
def donortable(request):
    # fields = ['Last_Name1', 'First_Name1', 'Last_Name2', 'First_Name2', 'Category']
    return render(request, 'donors.html', {'donortable': Contact.objects.filter(Q(Category='regular') | Q(Category='member') | Q(Category='first_time') | Q(Category='Annual') | Q(Category='grant') | Q(Category='otherdonor'))})
