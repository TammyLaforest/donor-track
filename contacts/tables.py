import django_tables2 as tables
from django.db import models
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from contacts.models import *

class contact_table_maker(tables.Table):
    class Meta:
        model = Contact
        template_name = 'contacts.html'

        def get_success_url(self):
            return reverse('/contacts.html')


def contact_table(request):
    table = contact_table_maker(Contact.objects.all( ))
    return render(request, 'contacts/contacts.html', {'contact_table': Contact.objects.filter(Q(Owner=request.user))})



class DonorTableMaker(tables.Table):
    class Meta:
        model = Contact
        template_name = 'contacts/donors.html'
        First_Name1 = tables.Column(order_by=('Last_Name'))

        def get_success_url(self):
            return reverse('contacts/donors.html')

def donor_table(request):
    table = DonorTableMaker(Contact.objects.all())
    return render(request, 'contacts/donors.html', {'donor_table': Contact.objects.filter(Q(Category='donor') and Q(Owner=request.user))})


class VendorTableMaker(tables.Table):
    class Meta:
        model = Contact
        template_name = 'contacts/vendors.html'

        def get_success_url(self):
            return reverse('contacts/vendors.html')

def vendor_table(request):
    table = VendorTableMaker(Contact.objects.all())
    return render(request, 'contacts/vendors.html', {'vendor_table': Contact.objects.filter(Q(Category='regular') | Q(Category='member') | Q(Category='first_time') | Q(Category='Annual') | Q(Category='grant') | Q(Category='otherdonor'))})



class DonorCategoriesTableMaker(tables.Table):
    class Meta:
        model = donor_categories
        template_name = 'contacts/donor_categories.html'

        def get_success_url(self):
            return reverse('contacts/donor_categories.html')

def donor_categories_table(request):
    table = DonorCategoriesTableMaker(Contact.objects.all())
    return render(request, 'contacts/donor_categories.html', {'donor_categories_table':Contact.objects.all()})

class VendorCategoriesTableMaker(tables.Table):
    class Meta:
        model = vendor_categories
        template_name = 'contacts/vendor_categories.html'

        def get_success_url(self):
            return reverse('contacts/vendor_categories.html')

def vendor_categories_table(request):
    table = VendorCategoriesTableMaker(Contact.objects.all())
    return render(request, 'contacts/vendor_categories.html', {'vendor_categories_table':Contact.objects.all()})
