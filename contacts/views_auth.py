
from django.db import models
# from django.db.models import Q
# from django.views import generic, View
# from django.views.generic import ListView, CreateView, DetailView, TemplateView

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

# from contacts.filters import *
# from contacts.forms import *
# from contacts.models import *
# from contacts.tables import *
# from contacts.views import *
# from contact.views_auth import *

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class ContactOwnerMixin(object):

    def get_object(self, queryset=None):
        """Returns the object the view is displaying.

        """

        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
            owner=self.request.user,
        )

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise PermissionDenied

        return obj
