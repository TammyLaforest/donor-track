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
import donors
from donors import views

import easydonorapp
import contacts

from easydonorapp import views
from contacts import views

from django.contrib.auth.models import User
# from contacts.views import donortable, ContactsTable
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include # new



    # url(r'^donors/', donortable),
    # url(r'^contacts/detail/', ContactsTable),

urlpatterns = [

    # Forms
    path('contacts/new_contact', contacts.views.contact_new_view.as_view(), name='new_contact'),

    # Tables
    path('contacts/', contacts.views.ContactListView.as_view(), name='contacts'),

    path('admin/', admin.site.urls),
    # path('contacts/new', TemplateView.as_view(template_name='new.html')),

    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('new/', TemplateView.as_view(template_name='new.html'), name='new'),

    path('accounts/', include('django.contrib.auth.urls')),



    path('accounts/', include('accounts.urls')),

    path('deposit/', donors.views.DepositView.as_view(),
        name='deposit',),
    path('donors/', donors.views.DonorsView.as_view(),
            name='donors',),
    path('donor_categories/', donors.views.Donor_Categories_View.as_view(),
            name='donor_categories',),
    path('thanks/', donors.views.Thanks_View.as_view(),
            name='thanks',),
    ]
