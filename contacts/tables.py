import django_tables2 as tables
from django.db import models
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from contacts.models import *

# sequence – reorder columns
# fields – specify model fields to include
# exclude – specify model fields to exclude

# Contact section
class contact_table_maker(tables.Table):
    class Meta:
        model = Contact
        template_name = 'contacts/contacts.html'

        def get_success_url(self):
            return reverse('contacts/contacts.html')


def contact_table(request):
    table = contact_table_maker(Contact.objects.all())
    return render(request, 'contacts/contacts.html', {'contact_table': Contact.objects.filter(Q(Owner=request.user))})

# Donor section

class DonorTableMaker(tables.Table):
    class Meta:
        model = Contact
        template_name = 'contacts/donors.html'
        First_Name1 = tables.Column(order_by=('First_Name1'))

        def get_success_url(self):
            return reverse('contacts/donors.html')




def donor_table(request):
    table = DonorTableMaker(Contact.objects.all())
    return render(request, 'contacts/donors.html', {'donor_table': Contact.objects.filter(Q(Category='regular') | Q(Category='member') | Q(Category='first_time') | Q(Category='Annual') | Q(Category='grant') | Q(Category='otherdonor'))})


class VendorTableMaker(tables.Table):
    class Meta:
        model = Contact
        template_name = 'contacts/vendors.html'

        def get_success_url(self):
            return reverse('contacts/vendors.html')

def vendor_table(request):
    table = VendorTableMaker(Contact.objects.all())
    return render(request, 'contacts/vendors.html', {'vendor_table': Contact.objects.filter(Q(Category='regular') | Q(Category='member') | Q(Category='first_time') | Q(Category='Annual') | Q(Category='grant') | Q(Category='otherdonor'))})

# def donor_category_table(request):
#     table = DonorTableMaker(Contact.objects.all())
#     return render(request, 'contacts/donor_categories.html', {'donor_category_table':Contact.objects.raw("SELECT First_Name1, Last_Name1, First_Name2, Last_Name2 FROM donortabletable")})
#
# def vendor_category_table(request):
#     table = DonorTableMaker(Contact.objects.all())
#     return render(request, 'contacts/vendor_categories.html', {'vendor_category_table':Contact.objects.raw("SELECT First_Name1, Last_Name1, First_Name2, Last_Name2 FROM donortabletable")})
