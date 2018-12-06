from django.db import models
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, reverse
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView, RedirectView
admin.autodiscover()

import contacts
from . import views, models, forms

urlpatterns = [

    path('search/', contacts.views.ContactListView.as_view(),name='search',),

    url(r'^contact/contacts/(?P<pk>\d+)/$', contacts.views.ContactListView.as_view(), name='contacts'),
    path('new_contact', contacts.views.contacts_new, name='new_contact'),
    path('<int:pk>/edit/', contacts.views.contacts_edit, name='edit'),

    path('contacts_list', contacts.views.ContactListView.as_view(), name="contacts_list"),
    path('donors/', contacts.views.DonorListView.as_view(), name='donors'),
    path('vendors/', contacts.views.VendorListView.as_view(), name='vendors'),

    # I should have namespaced this out of existance
    # path('contacts/', contacts.views.ContactListView.as_view(), name='contacts'),

    # Do I need separate URLs for each list or is it just one big sorted list?
    # url(r'^contact/donors/(?P<pk>\d+)/$', contacts.views.DonorListView.as_view(), name='donors'),

    ]
