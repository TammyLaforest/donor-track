from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib.auth import views as auth_views



# from tutorial https://wsvincent.com/django-user-authentication-tutorial-signup/


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('home/', views.SignUpHome.as_view(), name='home'),
    ]

# name="password_reset")
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
