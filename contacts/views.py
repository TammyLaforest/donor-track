from django.db import models
from django.db.models import Q
from .models import Contact


import django_filters
from django_filters.views import FilterView

import django_tables2 as tables
from django_tables2.views import SingleTableMixin


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views import generic
from django.views.generic import ListView, CreateView

from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required, permission_required

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

class ListContactView(ListView):
    list_display = ['__all__']
    model = Contact
    template_name = 'contacts.html'


# class ContactsTable(tables.Table):
#     class Meta:
#         model = Contact
        # template_name='contacts.html'
        # First_Name1 = tables.Column(order_by=('First_Name1'))
        # filterset_class = CoupleFilter
def ContactsTable(request):
        return render(request, 'contacts/contacts.html', {'ContactsTable': Contact.objects.filter(Q(Owner=request.user))})


class DonorTableMaker(tables.Table):
    class Meta:
        model = Contact
        template_name = 'donors.html'
        First_Name1 = tables.Column(order_by=('First_Name1'))


        def get_success_url(self):
            return reverse('donors.html')

def donortable(request):
    table = DonorTableMaker(Contact.objects.all())
    return render(request, 'donors.html', {'donortable': Contact.objects.filter(Q(Category='regular') | Q(Category='member') | Q(Category='first_time') | Q(Category='Annual') | Q(Category='grant') | Q(Category='otherdonor'))})


def donortableterble(request):
    return render(request, 'donors.html', {'donortable':Contact.objects.raw("SELECT First_Name1, Last_Name1, First_Name2, Last_Name2 FROM donortabletable")})
