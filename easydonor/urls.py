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
from easydonorapp import views
from easydonorapp.views import *
from easydonorapp.models import *

import contacts
from contacts import views, models
from contacts.models import *
from contacts.views import *

import users
from users.allauth.account import views, models, urls
from users.allauth.account.models import *
from users.allauth.account.views import *

authdir = users.allauth.account

urlpatterns = [
    #Include urls from other apps
    url(r'^account', include(('users.allauth.account.urls', 'users'), namespace='account')),


    path('account/', contacts.views.ContactListView.as_view(), name='contacts'),

    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
        name='signup'),
    url(r'^email-verification/$',
        TemplateView.as_view(template_name="email_verification.html"),
        name='email-verification'),
    url(r'^login/$', TemplateView.as_view(template_name="login.html"),
        name='login'),
    url(r'^logout/$', TemplateView.as_view(template_name="logout.html"),
        name='logout'),
    url(r'^password-reset/$',
        TemplateView.as_view(template_name="password_reset.html"),
        name='password-reset'),
    url(r'^password-reset/confirm/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password-reset-confirm'),

    url(r'^user-details/$',
        TemplateView.as_view(template_name="user_details.html"),
        name='user-details'),
    url(r'^password-change/$',
        TemplateView.as_view(template_name="password_change.html"),
        name='password-change'),


    # this url is used to generate email content
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),


    url(r'^account/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^account/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^account/profile/$', TemplateView.as_view(template_name='profile.html')),
    path('search/', contacts.views.ContactListView.as_view(),name='search',),


    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('nope/', TemplateView.as_view(template_name='nope.html'), name='nope'),
    path('deposit/', easydonorapp.views.DonorDepositView.as_view(),name='deposit',),
    path('deposit_list/', easydonorapp.views.DepositView.as_view(),name='deposit_list',),
    url(r'^(?P<pk>\d+)/$', easydonorapp.views.DonorListDepositView.as_view(), name='deposit_list'),
    path('contacts/', contacts.views.ContactListView.as_view(), name='contacts'),

    url(r'^contact/donors/(?P<pk>\d+)/$', contacts.views.DonorListView.as_view(), name='donors'),
    path('donors/', contacts.views.DonorListView.as_view(), name='donors'),
    path('vendors/', contacts.views.VendorListView.as_view(), name='vendors'),
    path('contacts/new', contacts.views.contacts_new, name='new'),
    path('<int:pk>/edit/', contacts.views.contacts_edit, name='edit'),
    # reverse('/accounts/login/')

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # This is how you view images from media folder.
