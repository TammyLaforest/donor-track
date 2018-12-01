"""easy-donor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url

import accounts
from accounts import views

import easydonorapp
import contacts
import testapp

from easydonorapp import views
from contacts import views
from testapp import views

from django.contrib.auth.models import User
# from contacts.views import donortable, ContactsTable
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include # new

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [



    # Test URLS to be deleted
    path('brand_model_select/', TemplateView.as_view(template_name='brand_model_select.html'), name='brand_model_select'),


    path('accounts/', include('django.contrib.auth.urls')),
    path('testapp/', include('testapp.urls')),

    # From urls.py in other apps
    path('accounts/', include('accounts.urls')),

    # Forms
    path('contacts/new_contact', contacts.views.contact_new_view.as_view(), name='new_contact'),
    path('contacts/new_donor', contacts.views.donor_new_view.as_view(), name='new_contact'),
    path('contacts/new_donor', contacts.views.vendor_new_view.as_view(), name='new_contact'),

    # Tables
    # url(r'^donors/', donortable),
    # url(r'^contacts/detail/', ContactsTable),


    #Urls by views
        #Contacts
    path('contacts/contacts/', contacts.views.ContactsView.as_view(), name='contacts'),
    path('contacts/donors/', contacts.views.DonorsView.as_view(),name='donors',),
    path('contacts/vendors/', contacts.views.VendorsView.as_view(),name='vendors',),

    path('contacts/donor_categories/', contacts.views.Donor_Categories_View.as_view(),name='donor_categories',),
    path('contacts/new_contact/', contacts.views.DonorsView.as_view(),name='new_contact',),
    path('contacts/new_donor/', contacts.views.DonorsView.as_view(),name='new_donor',),
    path('contacts/new_vendor/', contacts.views.DonorsView.as_view(),name='new_vendor',),

        #easydonorapp
    path('deposit/', easydonorapp.views.DepositView.as_view(),name='deposit',),
    path('thanks/', easydonorapp.views.Thanks_View.as_view(),name='thanks',),

    #Template As View

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),


    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # This is how you view images from media folder.
