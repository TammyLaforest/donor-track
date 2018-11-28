from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email
