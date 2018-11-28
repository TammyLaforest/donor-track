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
import easydonorapp
import contacts
import donors
from accounts import views
from easydonorapp import views
from contacts import views
from donors import views

from contacts.views import contactstable, donortable

from django.views.generic import TemplateView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    url(r'^contacts/', contactstable),
    url(r'^donors/', donortable),


    path('home/', TemplateView.as_view(template_name='home.html'),
        name='home'),
    path('', TemplateView.as_view(template_name='home.html'),
        name='home'),
    path('new/', TemplateView.as_view(template_name='new.html'),
            name='new'),
# url(r'^contacts/', contactstable),
    path('deposit/', donors.views.DepositView.as_view(),
        name='deposit',),

    path('contacts/', contacts.views.ListContactView.as_view(),
        name='contacts',),

    path('donors/', donors.views.DonorsView.as_view(),
            name='donors',),
    path('donor_categories/', donors.views.Donor_Categories_View.as_view(),
            name='donor_categories',),
    path('thanks/', donors.views.Thanks_View.as_view(),
            name='thanks',),

    path('accounts/', include('django.contrib.auth.urls')),




    ]
