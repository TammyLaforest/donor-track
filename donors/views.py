from django.shortcuts import render
from contacts.models import Contact
from accounts.models import User

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views import generic
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormView

from contacts.models import Contact


class donor_new_view(CreateView):
    model = Contact
    template_name = 'new_donor.html'
    fields = ['First_Name1', 'Last_Name1', 'First_Name2', 'Last_Name2', ]
    #
    def get_success_url(self):
        return reverse('new.html')



def donor_new(request):
    form = DonorForm()
    return render(request, 'contacts/new.html', {'form': form})

def donortable(request):
    table = DonorTableMaker(Contact.objects.all())
    return render(request, 'donors.html', {'donortable': Contact.objects.filter(Q(Category='regular') | Q(Category='member') | Q(Category='first_time') | Q(Category='Annual') | Q(Category='grant') | Q(Category='otherdonor'))})

class DepositView(CreateView):

    model = Contact
    template_name = 'deposit.html'
    fields ='__all__'

class DonorsView(CreateView):
    model = Contact
    template_name = 'donors.html'
    fields = '__all__'

class Donor_Categories_View(CreateView):
    model = Contact
    template_name = 'donor_categories.html'
    fields = '__all__'

class Thanks_View(CreateView):
    model = Contact
    template_name = 'thanks.html'
    fields = '__all__'
