from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email


# class Registered_User(models.Model):
#
#     owner = models.ForeignKey(User, on_delete = models.CASCADE)
#     uuid = ShortUUIDField(unique=True, primary_key = True,)
#     created_on = models.DateField(auto_now_add=True)
#
#     username = models.ForeignKey(max_length = 150, unique=True, on_delete = models.CASCADE)
#     password =
#     email = models.EmailField(validators=[validate_email], blank=True )
#
#     Title = models.CharField(max_length=10, blank=True )
#     first_name = models.CharField(max_length=30, blank=True )
#     last_name = models.CharField(max_length=30, blank=True )
#
#     address = models.CharField(max_length=255, blank=True)
#     city = models.CharField(max_length=255,blank=True)
#     state = models.CharField(max_length=2,blank=True)
#     postal_code = models.CharField(max_length=20,blank=True)

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#
# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
