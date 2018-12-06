
from __future__ import unicode_literals

import datetime

from django.core import signing
from django.db import models, transaction
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from django.conf import settings
# users/models.py


from django.contrib.auth.models import User
# https://docs.djangoproject.com/en/2.1/topics/auth/customizing/

class Profile(models.Model): #should this be models.Model?
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="Profile", null=True, blank=True)
    username = models.CharField(max_length=150,blank=False )
    email = models.CharField(max_length=150,blank=False )
    first_name = models.CharField(max_length=150,blank=False )
    last_name = models.CharField(max_length=150,blank=False )

    def my_view(request):
        username = None
        email = None
        first_name = None
        last_name = None
        if request.user.is_authenticated():
            username = get_username()
            email = get_email()
            first_name = get_first_name()
            last_name = get_last_name()

class BusinessProfile(models.Model): #should this be models.Model?
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="BusinessProfile", null=True, blank=True)
    business_name = models.CharField(max_length=150,blank=False )
    taxid = models.CharField(max_length=50, blank=True )
    Phone = models.CharField(max_length=50, blank=True )
    Address = models.CharField(max_length=255, blank=True)
    City = models.CharField(max_length=255,blank=True)
    State = models.CharField(max_length=2,blank=True)
    Postal_code = models.CharField(max_length=20,blank=True)
    Country = models.CharField(max_length=30, default='USA', blank=True )
