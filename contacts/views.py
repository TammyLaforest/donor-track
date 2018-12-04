from django.db import models
from django.db.models import Q
from django.views import generic, View
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.views.generic.edit import FormView

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.forms import inlineformset_factory, formset_factory, BaseInlineFormSet, ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

from django.contrib.auth.models import User
from contacts.models import *
from contacts.tables import *
from contacts.views_auth import *

from django.core.paginator import Paginator




#
# class contact_table_maker(tables.Table):
#     class Meta:
#         model = Contact
#         template_name = 'contacts.html'
#
#         def get_success_url(self):
#             return reverse('/contacts.html')
#
#
# def contact_table(request):
#     table = contact_table_maker(Contact.objects.all( ))
#     return render(request, 'contacts/contacts.html', {'contact_table': Contact.objects.filter(Q(Owner=request.user))})



# Main Contcts List as_view
class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 10

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get the context
        context = super(ContactListView, self).get_context_data(**kwargs)
        # paginator = Paginator(list_exam, self.paginate_by)
        # page = self.request.GET.get('page')
        #
        # try:
        #     file_exams = paginator.page(page)
        # except PageNotAnInteger:
        #     file_exams = paginator.page(1)
        # except EmptyPage:
        #     file_exams = paginator.page(paginator.num_pages)

        context['object_list'] = Contact.objects.filter(Q(Contact_Category='donor')).order_by('Last_Name')
        return context

class DonorListView(generic.ListView):
    model = Contact
def get_context_data(self, **kwargs):
    context = super(DonorListView, self).get_context_data(**kwargs)
    context['object_list'] = Contact.objects.filter(Q(Contact_Category='donor')).order_by('First_Name')
    return context

class VendorListView(generic.ListView):
    model = Contact
    def get_context_data(self, **kwargs):
        context = super(VendorListView, self).get_context_data(**kwargs)
        context['object_list'] = Contact.objects.filter(Q(Contact_Category='vendor')).order_by('Company')
        return context

class generic_contact_form(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


def contacts_new(request):
    if request.method == "POST":
        form = generic_contact_form(request.POST)
        if form.is_valid():
                Contact = form.save(commit=False)
                Contact.Owner = request.user
                Contact.Account = 'account'
                Contact.save()
                return redirect('contacts')
        else:
            return redirect('nope')

                # return redirect('contacts/detail',pk = uuid)
    else:
        form = generic_contact_form()
        return render(request, 'contacts/new.html', {'form': form})

def contacts_edit(request, pk):
    Contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = generic_contact_form(request.POST, instance=Contact)
        if form.is_valid():
            Contact = form.save(commit=False)
            Contact.Owner = request.user
            Contact.save()
            return redirect('edit', pk=Contact.uuid)
    else:
        form = generic_contact_form(instance=Contact)
    return render(request, '/edit.html', {'form': form})

# Views for forms
class contacts_new_view(FormView):
    template_name = 'new.html'
    form_class = generic_contact_form
    success_url = '/home/'

    def form_valid(self, form):
        def contacts_new():
            return super().form_valid(form)

class contacts_edit_view(FormView):
    template_name = 'edit.html'
    form_class = generic_contact_form
    success_url = '/home/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        def contacts_edit():
            return super().form_valid(form)


class donors_view(LoggedInMixin, ContactOwnerMixin, DetailView):
    model = Contact
    template_name = 'donors.html'
    fields = '__all__'


class donor_categories_view(LoggedInMixin, ContactOwnerMixin, DetailView):
    model = Contact
    template_name = 'contacts/donor_categories.html'
    fields = '__all__'

class vendor_categories_view(CreateView):
    model = Contact
    template_name = 'contacts/vendor_categories.html'
    fields = '__all__'


class vendors_view( LoggedInMixin, ContactOwnerMixin, DetailView):
    model = Contact
    template_name = 'vendors.html'
    fields = '__all__'

    # path('contacts/', views.contacts_view, name='contacts'),
    # path('contacts/new', views.contacts_new_view, name='new'),
    # path('contacts/<int:pk>/', views.contacts_detail_view, name='detail'),
    # path('contacts/<int:pk>/edit/', views.contacts_edit_view, name='edit'),


# class new_donor_individual_form(ModelForm):
#     class Meta:
#         model = Contact
#         Owner=User
#         Contact_Format = 'Individual'
#         Account = 'Last_Name'+'', ''+ 'First_Name'
#         fields = '__all__'
#         exclude =['First_Name2', 'Last_Name2', 'Phone2', 'Email2', 'Company', 'Owner', 'Category', 'Vendor_Subcategory', 'Contact_Format' ]
#
# class new_donor_couple_form(ModelForm):
#     class Meta:
#         model = Contact
#         Owner=User
#         Contact_Format = 'Couple'
#         Account = 'Last_Name'+'', ''+ 'First_Name' + '&' + 'Last_Name2'+'', ''+ 'First_Name2'
#         fields = '__all__'
#         exclude =[ 'Company', 'Owner', 'Category', 'Vendor_Subcategory', 'Contact_Format' ]
#
# # Views for forms
# def contact_new(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = generic_contact_form(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/contacts/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = generic_contact_form()
#
#     return render(request, 'contacts/new_contact_generic.html', {'form': form})
#

# class contact_new_generic_view(CreateView):
#     Owner = User
#     form_class= generic_contact_form
#     template_name = 'contacts/new_contact_generic.html'
#     return HttpResponseRedirect('/contacts/')
#
#     def get_success_url(self):
#         return redirect('contacts')
