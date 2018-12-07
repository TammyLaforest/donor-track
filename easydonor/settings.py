"""
Django settings for easydonor project.
Generated by 'django-admin startproject' using Django 2.1.3.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.conf import settings


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yh4g1h-u+q3(v*uddud_0@ka%u0u0%y@c&aq1s4+a2g*v9fr0$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

INSTALLED_APPS = [


    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.admin',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',

    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'shortuuidfield',
    'crispy_forms',


    'easydonorapp',
    'contacts',
    'users',



]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'easydonor.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap'

TEMPLATES = [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'loaders': [

            ('django.template.loaders.cached.Loader', [
            'admin_tools.template_loaders.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',

            ]),
        ],
        },
    }]

WSGI_APPLICATION = 'easydonor.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FORM_RENDERER ='django.forms.renderers.DjangoTemplates'

# https://medium.com/@gajeshbhat/django-allauth-setup-and-configuration-tutorial-63417bba339c
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ]
# STATICFILES_FINDERS ='django.contrib.staticfiles.finders.AppDirectoriesFinder'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# MEDIA_ROOT = '/Users/user/Envs/easydonor/static/easydonorapp/easydonorapp/media/'
# MEDIA_URL = "http://127.0.0.1:8000/easydonorapp/media/"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"

#all-auth registraion settings
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =7
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400 # 1 day. This does ot prevent admin login frombeing brut forced.
ACCOUNT_LOGOUT_REDIRECT_URL ='/account/login/' #or any other page
LOGIN_REDIRECT_URL = '/account/email/' # redirects to profile page by default
ACCOUNT_PRESERVE_USERNAME_CASING = False # reduces the delays in iexact lookups
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL=True
ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_USERNAME_REQUIRED =True
ACCOUNT_USERNAME_VALIDATORS = None
APPEND_SLASH = True

ACCOUNT_ADAPTER = 'allauth.account.adapter.DefaultAccountAdapter'


ACCOUNT_FORMS = {
'login': 'allauth.account.forms.LoginForm',
'signup': 'allauth.account.forms.SignupForm',
'add_email': 'allauth.account.forms.AddEmailForm',
'change_password': 'allauth.account.forms.ChangePasswordForm',
'set_password': 'allauth.account.forms.SetPasswordForm',
'reset_password': 'allauth.account.forms.ResetPasswordForm',
'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
}
# SOCIALACCOUNT_FORMS = {
# 'login': 'allauth.socialaccount.forms.DisconnectForm',
# 'signup': 'allauth.socialaccount.forms.SignupForm',
# }
#Social Account Settings
# SOCIALACCOUNT_PROVIDERS = {
    # 'facebook': {
    #     'METHOD': 'oauth2',
    #     'SCOPE': ['email', 'public_profile', 'user_friends'],
    #     'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    #     'INIT_PARAMS': {'cookie': True},
    #     'FIELDS': [
    #         'id',
    #         'email',
    #         'name',
    #         'first_name',
    #         'last_name',
    #         'verified',
    #         'locale',
    #         'timezone',
    #         'link',
    #         'gender',
    #         'updated_time',
    #     ],
    #     'EXCHANGE_TOKEN': True,
    #     'LOCALE_FUNC':  lambda request: 'en-US',
    #     'VERIFIED_EMAIL': False,
    #     'VERSION': 'v2.12',
    # },
#      'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         }
#     }
# }
# SOCIALACCOUNT_QUERY_EMAIL=ACCOUNT_EMAIL_REQUIRED
# SOCIALACCOUNT_EMAIL_REQUIRED=ACCOUNT_EMAIL_REQUIRED
# SOCIALACCOUNT_STORE_TOKENS=False



# demo_project/settings.py
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
#
# SOCIALACCOUNT_ENABLED = 'allauth.socialaccount' in settings.INSTALLED_APPS
#
# LOGIN_REDIRECT_URL = getattr(settings, 'LOGIN_REDIRECT_URL', '/')


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
#
AUTH_USER_MODEL = 'auth.User'
# USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
USER_MODEL = AUTH_USER_MODEL
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'
LOGOUT_REDIRECT_URL = '/logout'
#
# EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
