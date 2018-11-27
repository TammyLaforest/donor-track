from easydonorapp.models import Contact

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views import generic
from django.views.generic import ListView, CreateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


class ListContactView(ListView):

    model = Contact
    template_name = 'contacts.html'

class CreateContactView(CreateView):

    model = Contact
    template_name = 'edit_contact.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('contacts-list')

class IndexView(CreateView):

    model = Contact
    template_name = 'index.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('contacts-list')

class DepositView(CreateView):

    model = Contact
    template_name = 'deposit.html'
    fields = '__all__'




class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

# class LoginView(CreateView):
#
#     model = User
#     template_name = 'index.html'
#     fields = '__all__'
#
#     def get_success_url(self):
#         return reverse('contacts-list')
