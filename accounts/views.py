from __future__ import unicode_literals

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

from django.urls import reverse_lazy

from django.views import generic
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.views.generic.edit import FormView

from django.forms import inlineformset_factory, formset_factory, BaseInlineFormSet, ModelForm

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, PermissionsMixin

from django.db import models, transaction
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _

# from easydonor.accounts.models import User, Profile
from contacts.models import *

# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#proxy
# users = User.objects.all().select_related('profile')


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
#
#
# class profile_view(TemplateView):
#     model = Profile
#     template_name = 'profile.html'
#     fields = '__all__'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
