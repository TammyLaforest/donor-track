from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.forms import ModelForm
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from .models import *

# from tutorial https://wsvincent.com/django-user-authentication-tutorial-signup/

class profile_form(ModelForm):
    class Meta:
        model = profile
        fields = '__all__'

def edit_profile_view(request):
    form = profile_form()
    return render(request, 'accounts/edit_profile.html', {'form': form})
    success_url = reverse_lazy('profile')

class profile_view(TemplateView):
    model = profile
    template_name = 'profile.html'
    fields = '__all__'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
