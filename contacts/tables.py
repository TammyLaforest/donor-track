from django.db import models
from django.db.models import Q
from .models import Contact
from django.http import HttpResponse





def ContactsTable(request):
        return render(request, 'contacts/contacts.html', {'ContactsTable': Contact.objects.filter(Q(Owner=request.user))})


class DonorTableMaker(tables.Table):
    class Meta:
        model = Contact
        template_name = 'contacts/donors.html'
        First_Name1 = tables.Column(order_by=('First_Name1'))


        def get_success_url(self):
            return reverse('contacts/donors.html')


def donortableterble(request):
    return render(request, 'contacts/donors.html', {'donortable':Contact.objects.raw("SELECT First_Name1, Last_Name1, First_Name2, Last_Name2 FROM donortabletable")})


# def donortable(request):
#     table = DonorTableMaker(Contact.objects.all())
#     return render(request, 'donors.html', {'donortable': Contact.objects.filter(Q(Category='regular') | Q(Category='member') | Q(Category='first_time') | Q(Category='Annual') | Q(Category='grant') | Q(Category='otherdonor'))})
#
#
# def ContactsTable(request):
#     return render(request, 'contacts/detail.html', {'ContactsTable': Contact.objects.filter(Q(Owner=request.user))})
