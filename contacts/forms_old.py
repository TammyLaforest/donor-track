import django_filters

from django.db import models
from django.db.models import Q
from django.views import generic, View
from django.forms import inlineformset_factory, formset_factory, BaseInlineFormSet
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

from contacts.filters import *
from contacts.tables import *
from contacts.models import *
from contacts.views import *
from contacts.views_auth import *


class contact_form(ModelForm):
    class Meta:
        model = Contact
        exclude = ()

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # This is crucial.

        helper.layout = Layout(
            Fieldset('Create new contact', 'name'),
        )

        return helper

        def manage_individual_form_set(request, Contact):
            Contact = Contact.objects.get(pk=uuid)
            contact_individual_form_set = inlineformset_factory(
                Contact,
                Individual,
                Address,
                fields = '__all__')
            if request.method == "POST":
                formset = contact_individual_form_set(request.POST, request.FILES, instance=contact)
                if formset.is_valid():
                    formset.save()
                    # Do something. Should generally end with a redirect. For example:
                    return HttpResponseRedirect(contact.get_absolute_url())
            else:
                formset = contact_individual_form_set(instance=contact)
            return render(request, 'donors.html', {'formset': formset})

        def manage_couple_form_set(request, Contact):
            Contact = Contact.objects.get(pk=uuid)
            contact_couple_form_set = inlineformset_factory(
                Contact,
                Spouse,
                Address,
                fields = '__all__')
            if request.method == "POST":
                formset = contact_couple_form_set(request.POST, request.FILES, instance=contact)
                if formset.is_valid():
                    formset.save()
                    # Do something. Should generally end with a redirect. For example:
                    return HttpResponseRedirect(contact.get_absolute_url())
            else:
                formset = contact_couple_form_set(instance=contact)
            return render(request, 'donors.html', {'formset': formset})

        def manage_other_form_set(request, Contact):
            Contact = Contact.objects.get(pk=uuid)
            contact_other_form_set = inlineformset_factory(
                Contact,
                Other,
                Address,
                fields = '__all__')
            if request.method == "POST":
                formset = contact_other_form_set(request.POST, request.FILES, instance=contact)
                if formset.is_valid():
                    formset.save()
                    # Do something. Should generally end with a redirect. For example:
                    return HttpResponseRedirect(contact.get_absolute_url())
            else:
                formset = contact_other_form_set(instance=contact)
            return render(request, 'donors.html', {'formset': formset})


        def manage_vendors(request, Contact_uuid):
            Contact = get_object_or_404(models.Contact, id=Contact_uuid)

            if request.method == 'POST':
                formset = forms.contact_vendor_form_set(request.POST, instance=Contact)
                if formset.is_valid():
                    formset.save()
                    return redirect('home', Contact_uuid=Contact_uuid)
            else:
                formset = forms.contact_vendor_form_set(instance=contact)

            return render(request, 'vendors.html', {
                          'Contact':Contact,
                          'vendors_formset':formset})


        def manage_vendor_form_set(request, Contact):
            Contact = Contact.objects.get(pk=uuid)
            contact_vendor_form_set = inlineformset_factory(
                Contact,
                Company_Vendor,
                Address,
                fields = '__all__')
            if request.method == "POST":
                formset = contact_vendor_form_set(request.POST, request.FILES, instance=contact)
                if formset.is_valid():
                    formset.save()
                    # Do something. Should generally end with a redirect. For example:
                    return HttpResponseRedirect(contact.get_absolute_url())
            else:
                formset = contact_vendor_form_set(instance=contact)
            return render(request, 'new_vendor.html', {'formset': formset})

        def manage_company_form_set(request, Contact):
            Contact = Contact.objects.get(pk=uuid)
            contact_company_form_set = inlineformset_factory(
                Contact,
                Company_Donor,
                Address,
                fields = '__all__')
            if request.method == "POST":
                formset = contact_company_form_set(request.POST, request.FILES, instance=contact)
                if formset.is_valid():
                    formset.save()
                    # Do something. Should generally end with a redirect. For example:
                    return HttpResponseRedirect(contact.get_absolute_url())
            else:
                formset = contact_company_form_set(instance=contact)
            return render(request, 'donors.html', {'formset': formset})


        class ContactVendorList(ListView):
            model = Contact

        class VendorContactCreate(CreateView):
            model = Contact
            fields = ['__all__']
            success_url = reverse_lazy('contacts')

        def get_context_data(self, **kwargs):
            data = super(VendorContactCreate, self).get_context_data(**kwargs)
            if self.request.POST:
                data['vendor_contacts'] = contact_vendor_form_set(self.request.POST)
            else:
                data['vendor_contacts'] = contact_vendor_form_set()
            return data

        def form_valid(self, form):
            context = self.get_context_data()
            vendor_contacts = context['vendor_contacts']
            with transaction.atomic():
                self.object = form.save()

                if vendor_contacts.is_valid():
                    vendor_contacts.instance = self.object
                    vendor_contacts.save()
            return super(VendorContactCreate, self).form_valid(form)



# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'
#
# class DonorForm(ModelForm):
#     class Meta:
#         model = Donor
#         fields = '__all__'
#
# class VendorForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'


# class PartialAuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         exclude = ['title']

def contact_new(request):
    form = contact_other_form_set()
    return render(request, 'contacts/new_contact.html', {'form': form})


def donor_new(request):
    form = contact_couple_form_set()
    return render(request, 'contacts/new_donor.html', {'form': form})


def vendor_new(request):
    form = contact_vendor_form_set()
    return render(request, 'contacts/new_vendor.html', {'form': form})
