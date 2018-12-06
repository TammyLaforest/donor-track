from django.db import models
from django.conf import settings
from django.db.models import Q
from django.views import generic, View
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django import forms
from django.forms import ModelForm
from contacts.models import Contact
from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import redirect
from django.urls import reverse
def my_view(request):
    ...
    obj = MyModel.objects.get(...)
    return redirect(obj, permanent=True)


# pages/views.py
class HomePageView(TemplateView):
    template_name = 'home.html'


class Thanks_View(CreateView):
    model = Contact
    template_name = 'thanks.html'
    fields = '__all__'

class DepositView(CreateView):

    model = Contact
    template_name = 'deposit.html'
    fields ='__all__'

class DonorDepositView(generic.ListView):
    model = Contact
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(DonorDepositView, self).get_context_data(**kwargs)
        # Need Paginator info
        context['object_list'] = Contact.objects.filter(Q(Contact_Category='donor')).order_by('Last_Name')
        return context


class DonorListDepositView(DetailView):
    model = Contact

    def get_deposit_data(self, **kwargs):
        context = super(DonorListDepositView, self).get_deposit_data(**kwargs)
        context['object_list'] = Contact.objects.filter(Q(Contact_Category='donor')).order_by('Last_Name')
        return context
