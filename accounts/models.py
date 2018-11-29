from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email


class User(models.Model):

    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    uuid = ShortUUIDField(unique=True, primary_key = True,)
    created_on = models.DateField(auto_now_add=True)
