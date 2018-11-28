from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email

# class Donor(models.Model):
#     Owner = models.ForeignKey(User, on_delete = models.CASCADE)
#
#     class Meta:
#         Owner =
#         unique_together = (("category","owner"),)
#     # category = models.ForeignKey(Category, on_delete = models.CASCADE)
#
#     models.ForeignKey('contacts.uuid', on_delete = models.CASCADE )

# if request.POST.get('foo') == 'bar':
#    print 'Bar'
    # def clean(self):
    #     if not (self.Company or
    #         self.First_Name1 or
    #         self.Last_Name1 or
    #         self.Last_Name2 or
    #         self.First_Name2):
    #         raise ValidationError("You must specify a contact name")
