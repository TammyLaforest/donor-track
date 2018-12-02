from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email


class profile(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    first_name = models.CharField(max_length=30 )
    last_name = models.CharField(max_length=30 )

    email = models.EmailField(validators=[validate_email] )

    company = models.CharField(max_length=115 )

    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255,blank=True)
    state = models.CharField(max_length=2,blank=True)
    postal_code = models.CharField(max_length=20,blank=True)

    taxid = models.CharField(max_length=100 )
