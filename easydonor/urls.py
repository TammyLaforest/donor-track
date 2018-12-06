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
from django.db import models
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, reverse
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView, RedirectView
admin.autodiscover()



import easydonorapp
from easydonorapp import views, models, forms
import contacts
from contacts import views, models, forms

import users
from users.allauth.account import urls
# from users.allauth.account import views, models, urls
# from users.allauth.account.models import *
# from users.allauth.account.views import *

authdir = users.allauth.account


urlpatterns = [

    #Include urls from other apps - contacts and users
    url(r'^account', include(('users.allauth.account.urls', 'users'), namespace='account')),
    # path('search/', contacts.views.ContactListView.as_view(),name='search',),
    path('contact-list/', contacts.views.ContactListView.as_view(), name="contact-list"),
    path('contacts/<int:pk>', contacts.views.ContactDetailView.as_view(), name='contact-detail'),
    path('contact/<int:pk>', contacts.views.ContactDetailView.as_view(), name='contact-detail'),

    path('new_contact', contacts.views.contacts_new, name='new_contact'),
    path('<int:pk>/edit/', contacts.views.contacts_edit, name='edit'),

    path('contacts/', contacts.views.ContactListView.as_view(), name='contacts'),
    path('donors/', contacts.views.DonorListView.as_view(), name='donors'),
    path('vendors/', contacts.views.VendorListView.as_view(), name='vendors'),


    # Home page main index
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', TemplateView.as_view(template_name='home.html')),

    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    # Error page
    path('nope/', TemplateView.as_view(template_name='nope.html'), name='nope'),

    # Related to deposit slip/donation taker
    path('deposit/', easydonorapp.views.DonorDepositView.as_view(),name='deposit',),
    # path('deposit_list/', easydonorapp.views.DepositView.as_view(),name='deposit_list',),
    url(r'^(?P<pk>\d+)/$', easydonorapp.views.DonorListDepositView.as_view(), name='deposit_list'),

    url(r'^account/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),



    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # This is how you view images from media folder.
