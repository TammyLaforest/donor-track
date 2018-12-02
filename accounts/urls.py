from django.urls import path, include
from django.views.generic import TemplateView
from accounts import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib.auth import views as auth_views



# from tutorial https://wsvincent.com/django-user-authentication-tutorial-signup/


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    # path('edit_profile/', views.profile_new.as_view(), name='edit_profile'),
    # path('edit_profile/', views.profile_new.as_view(), name='edit_profile'),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('edit_profile/', TemplateView.as_view(template_name='edit_profile.html'), name='edit_profile'),

    # path('accounts/edit_profile/', views.edit_profile_view.as_view(),name='edit_profile',),
    # path('accounts/profile/', views.profile_view.as_view(),name='profile',),

    # url(r'^accounts/profile/', profile_table),
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
