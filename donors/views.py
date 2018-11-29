from django.shortcuts import render
from contacts.models import Contact
from accounts.models import User

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views import generic
from django.views.generic import ListView, CreateView

# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm


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

    # User.objects.filter(
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
