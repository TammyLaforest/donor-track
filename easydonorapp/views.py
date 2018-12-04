from contacts.models import Contact

from django.db import models
# from django.db.models import Q
from django.views import generic, View
from django.views.generic import ListView, CreateView, DetailView, TemplateView

class DepositView(CreateView):

    model = Contact
    template_name = 'deposit.html'
    fields ='__all__'


class Thanks_View(CreateView):
    model = Contact
    template_name = 'thanks.html'
    fields = '__all__'

class DonorListDepositView(DetailView):
    model = Contact

    def get_deposit_data(self, **kwargs):
        context = super(DonorListDepositView, self).get_deposit_data(**kwargs)
        context['object_list'] = Contact.objects.filter(Q(Contact_Category='donor')).order_by('Last_Name')
        return context
