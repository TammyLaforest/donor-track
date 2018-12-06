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


class Thanks_View(CreateView):
    model = Contact
    template_name = 'thanks.html'
    fields = '__all__'
