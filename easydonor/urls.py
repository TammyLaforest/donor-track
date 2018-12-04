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

import contacts
from contacts import views, tables, models
from contacts.tables import *
from contacts.models import Contact
from contacts.views import *

from django.contrib.auth.models import User

from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),

    path('deposit/', easydonorapp.views.DepositView.as_view(),name='deposit',),

    # From urls.py in other apps
    path('accounts/', include('accounts.urls')),
    # url(r'^$', ContactsListView.as_view(), name='contacts'),


    # path('', views.post_list, name='post_list'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),


    # url(r'^contacts/', contact_table),
    # path('contacts/', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
    path('contacts/', views.BookListView.as_view(), name='contacts'),
    path('contacts/<int:pk>/', views.contacts_detail_view, name='detail'),
    path('new', views.contacts_new, name='new'),
    path('<int:pk>/edit/', views.contacts_edit, name='edit'),

    # path('new_contact_generic/', contacts.views.contact_new_generic_view.as_view(),name='new_contact_generic',),
    # path('new_contact_generic/', TemplateView.as_view(template_name='new_contact_generic.html'), name='new_contact_generic'),

    # Other Tables


    url(r'^donors/', donor_table),
    path('donors/', TemplateView.as_view(template_name='donors.html'), name='donors'),

    url(r'^contacts/vendors/',vendor_table),
    path('contacts/vendors/', contacts.views.vendors_view.as_view(),name='vendors',),

    url(r'^contacts/vendor_categories/',vendor_categories_table),
    path('contacts/vendor_categories/', contacts.views.vendor_categories_view.as_view(),name='vendor_categories',),

    url(r'^contacts/donor_categories/',donor_categories_table),
    path('contacts/donor_categories/', contacts.views.donor_categories_view.as_view(),name='donor_categories',),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # This is how you view images from media folder.
