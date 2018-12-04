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
from easydonorapp import views
from easydonorapp.views import *

import contacts
from contacts import views, models
from contacts.models import Contact
from contacts.views import *

from django.contrib.auth.models import User

from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django_filters.views import FilterView

urlpatterns = [

    # url(r'^search/', include('haystack.urls')),
    # url(r'^/search/?$', MySearchView.as_view(), name='search_view'),
    path('search/', views.ContactListView.as_view(),name='search',),

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('nope/', TemplateView.as_view(template_name='nope.html'), name='nope'),
    path('deposit/', contacts.views.DonorDepositView.as_view(),name='deposit',),

    path('deposit_list/', contacts.views.DepositView.as_view(),name='deposit_list',),
    url(r'^(?P<pk>\d+)/$', contacts.views.DonorListDepositView.as_view(), name='deposit_list'),

    path('accounts/', include('accounts.urls')),

    path('contacts/', views.ContactListView.as_view(), name='contacts'),

    path('contacts/donors/', views.donors_view.as_view(), name='donors'),
    url(r'^contact/donors/(?P<pk>\d+)/$', views.DonorListView.as_view(), name='donors'),

    path('vendors/', views.VendorListView.as_view(), name='vendors'),

    path('contacts/new', views.contacts_new, name='new'),

    path('<int:pk>/edit/', views.contacts_edit, name='edit'),


    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # This is how you view images from media folder.

        # url(r'^$', ContactsListView.as_view(), name='contacts'),




        # url(r'^contacts/', contact_table),
        # path('contacts/', TemplateView.as_view(template_name='contacts.html'), name='contacts'),


        # path('contacts/<int:pk>/', views.contacts_detail_view, name='detail'),

        # path('new_contact_generic/', contacts.views.contact_new_generic_view.as_view(),name='new_contact_generic',),
        # path('new_contact_generic/', TemplateView.as_view(template_name='new_contact_generic.html'), name='new_contact_generic'),

        # Other Tables


        # url(r'^donors/', donor_table),
        # path('donors/', TemplateView.as_view(template_name='donors.html'), name='donors'),
