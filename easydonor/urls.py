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
from django.urls import path, include
from django.conf.urls import include, url

import easydonorapp
from easydonorapp import views
from easydonorapp.views import *
from easydonorapp.models import *

import contacts
from contacts import views, models
from contacts.models import *
from contacts.views import *

from django.contrib import admin
from django.urls import path, include


from django.conf.urls.static import static



urlpatterns = [


    path('', include('easydonorapp.urls')),
    path('users', include('users.urls')),
    path('accounts/', include('allauth.urls')),

    path('admin/', admin.site.urls),

    path('search/', views.ContactListView.as_view(),name='search',),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('nope/', TemplateView.as_view(template_name='nope.html'), name='nope'),
    path('deposit/', easydonorapp.views.DonorDepositView.as_view(),name='deposit',),
    path('deposit_list/', easydonorapp.views.DepositView.as_view(),name='deposit_list',),
    url(r'^(?P<pk>\d+)/$', easydonorapp.views.DonorListDepositView.as_view(), name='deposit_list'),
    path('contacts/', views.ContactListView.as_view(), name='contacts'),
    url(r'^contact/donors/(?P<pk>\d+)/$', views.DonorListView.as_view(), name='donors'),
    path('donors/', views.DonorListView.as_view(), name='donors'),
    path('vendors/', views.VendorListView.as_view(), name='vendors'),
    path('contacts/new', views.contacts_new, name='new'),
    path('<int:pk>/edit/', views.contacts_edit, name='edit'),


    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # This is how you view images from media folder.
