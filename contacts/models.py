from django.db import models
from django import forms

from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email
from django.forms import ModelForm

from django.contrib.auth.models import User
from model_utils import Choices

# Generic contact model
class Contact(models.Model):
    Owner = models.ForeignKey(User, on_delete = models.CASCADE)
    uuid = ShortUUIDField(unique=True, primary_key = True,)
    Created_On = models.DateField(auto_now_add=True)
    CATEGORY_CHOICES = ( ('donor', 'Donor'), ('vendor', 'Vendor'))

    Contact_Category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Donor',
    )

    Address = models.CharField(max_length=255, blank=True)
    City = models.CharField(max_length=255,blank=True)
    State = models.CharField(max_length=2,blank=True)
    Postal_code = models.CharField(max_length=20,blank=True)
    Country = models.CharField(max_length=30, default='USA', blank=True )

    Company = models.CharField(max_length=50,blank=True )

    First_Name = models.CharField(max_length=30, blank=True )
    Last_Name = models.CharField(max_length=30, blank=True )
    Email = models.EmailField(validators=[validate_email], blank=True )
    Phone = models.CharField(max_length=20, blank=True )

    First_Name2 = models.CharField(max_length=30, blank=True )
    Last_Name2 = models.CharField(max_length=30, blank=True )
    Phone2 = models.CharField(max_length=20, blank=True )
    Email2 = models.EmailField(validators=[validate_email], blank=True )
    Note = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Contacts'
        unique_together = (("Last_Name", "First_Name"),)
        unique_together = (("Last_Name2", "First_Name2"),)
        unique_together = (("Company", "Owner"),)


class Format(models.Model):
    FORMAT_CHOICES = (
        ('business', 'Business'),
        ('individual','Individual'),
        ('couple', 'Couple'),
        ('other', 'Other'),
    )
    Format = models.CharField(
        max_length=20,
        choices=FORMAT_CHOICES,
        default='Other',
    )
