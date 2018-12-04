from django.db import models
from django import forms

from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email
from django.forms import ModelForm

from django.contrib.auth.models import User

import contacts
from contacts.models import Contact
# from contacts.models import Contact
