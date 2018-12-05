from django.db import models, transaction
from django.conf import settings

from  .views import users
from easydonor import users
from easydonor.views import users

from django.urls import reverse_lazy

from django.views import generic
from django.views.generic import CreateView, TemplateView

from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth import views as auth_views
from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# class RequestViews(request):
#     model = User
#     template = 'auth.html'
#     # user = request.user
#     user_list = ezMap.objects.get(map_name = user.username)
