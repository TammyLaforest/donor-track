from django.db import models
from django.db.models import Q
from .models import Contact
from django.http import HttpResponse

import django_tables2 as tables
from django_tables2.views import SingleTableMixin



def ContactsTable(request):
        return render(request, 'contacts/contacts.html', {'ContactsTable': Contact.objects.filter(Q(Owner=request.user))})


class DonorTableMaker(tables.Table):
    class Meta:
        model = Contact
        template_name = 'donors.html'
        First_Name1 = tables.Column(order_by=('First_Name1'))


        def get_success_url(self):
            return reverse('donors.html')


def donortableterble(request):
    return render(request, 'donors.html', {'donortable':Contact.objects.raw("SELECT First_Name1, Last_Name1, First_Name2, Last_Name2 FROM donortabletable")})
