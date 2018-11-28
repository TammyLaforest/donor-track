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

from django.views.generic import TemplateView

urlpatterns = [
    path('home/', TemplateView.as_view(template_name='home.html'),
        name='home'),
    path('', TemplateView.as_view(template_name='home.html'),
        name='home'),
    path('admin/', admin.site.urls),
    path('contacts/', contacts.views.ListContactView.as_view(),
        name='contacts-list',),
    path('new/', contacts.views.CreateContactView.as_view(),
        name='contacts-new',),
    path('deposit/', donors.views.DepositView.as_view(),
        name='deposit',),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('signup/', accounts.views.SignUpView.as_view(),
    #     name='signup'),
    ]


# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
