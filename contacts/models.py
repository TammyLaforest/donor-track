from django.db import models
from django import forms

from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email
from django.forms import ModelForm

from django.contrib.auth.models import User
from model_utils import Choices

# Generic contact model
class Contact(models.Model):
    Owner = models.ForeignKey(User, on_delete = models.CASCADE)
    uuid = ShortUUIDField(unique=True, primary_key = True,)
    Created_On = models.DateField(auto_now_add=True)
    CATEGORY_CHOICES = ( ('donor', 'Donor'), ('vendor', 'Vendor'))

    Contact_Category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Donor',
    )

    Address = models.CharField(max_length=255, blank=True)
    City = models.CharField(max_length=255,blank=True)
    State = models.CharField(max_length=2,blank=True)
    Postal_code = models.CharField(max_length=20,blank=True)
    Country = models.CharField(max_length=30, default='USA', blank=True )

    Company = models.CharField(max_length=50,blank=True )

    First_Name = models.CharField(max_length=30, blank=True )
    Last_Name = models.CharField(max_length=30, blank=True )
    Email = models.EmailField(validators=[validate_email], blank=True )
    Phone = models.CharField(max_length=20, blank=True )

    First_Name2 = models.CharField(max_length=30, blank=True )
    Last_Name2 = models.CharField(max_length=30, blank=True )
    Phone2 = models.CharField(max_length=20, blank=True )
    Email2 = models.EmailField(validators=[validate_email], blank=True )
    Note = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Contacts'
        unique_together = (("Last_Name", "First_Name"),)
        unique_together = (("Last_Name2", "First_Name2"),)
        unique_together = (("Company", "Owner"),)


INCOME_CATEGORY_CHOICES = Choices(
('donation', 'Donation'),
('grant', 'Grant'),
('fundraiser', 'Fundraiser'),
('product', 'Product'),
('other_income', 'Other_Income'),

)

BANK_ACCOUNT_CHOICES = Choices (
('checking_account', 'Checking_Account'),
('savings_account', 'Savings_Account')
)

PAYMENT_CHOICES =  Choices (
('cash', 'Cash'),
('credit', 'Credit'),
('check', 'Check'),
('paypal', 'PayPal'),
('other_payment', 'Other_Payment')
)
FEES_CHOICES =  Choices (
('paypal_fees', '{PayPal_Fees}'),
('credit_fee', 'Credit_Fee'),
('service_fee', 'Service_Fee'),
('bank_fee', 'Bank_Fee'),
('other_fee', 'Other_Payment')
)

# class Pledge_collection(models.Model):
#     owner = models.ForeignKey(User, on_delete = models.CASCADE)
#     donor = models.OneToOneField(Contact, on_delete = models.CASCADE, primary_key=True, unique=True)

class Pledges(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    donor = models.ForeignKey(Contact, on_delete=models.CASCADE)
    pledge_number = models.AutoField(primary_key=True)
    pledge_date = models.DateField(auto_now_add=True, blank=False)
    pledge_amount = models.DecimalField(max_digits= 8, decimal_places=2)
    income_category = models.CharField(
            max_length=100,
            choices= INCOME_CATEGORY_CHOICES,
            default='Donation')
    note = models.TextField(blank=True)
    pledge_balance = models.DecimalField(max_digits= 8, decimal_places=2)
    payments_applied = models.DecimalField(max_digits= 8, decimal_places=2)


class DepositSlip(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    deposit_number = models.AutoField(primary_key=True, unique=True)
    deposit_date = models.DateField(auto_now_add=True, blank=False)
    bank_account = models.CharField(
            max_length=100,
            choices=BANK_ACCOUNT_CHOICES,
            default='Checking_Account')
    total_fees = models.DecimalField(max_digits= 8, decimal_places=2)
    total_income = models.DecimalField(max_digits= 8, decimal_places=2)
    net_deposit = models.DecimalField(max_digits= 8, decimal_places=2)
    cash_back = models.DecimalField(max_digits= 8, decimal_places=2)


class Payments(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, blank=False)
    donor = models.OneToOneField(Contact, on_delete = models.CASCADE, blank=False)
    deposit_number = models.ForeignKey(DepositSlip, on_delete=models.CASCADE, blank=False)
    payment_number = models.AutoField(primary_key=True)
    payment_date = models.DateField(auto_now_add=True, blank=False)
    apply_payment_to = models.ManyToManyField(Pledges, blank=False)
    payment_method = models.CharField(
            max_length=100,
            choices=PAYMENT_CHOICES,
            default="Check",
            blank=False)
    payment_reference = models.CharField(max_length=255,blank=True)
    payment_amount = models.DecimalField(max_digits= 8, decimal_places=2, blank=False)
    fees_source = models.CharField(
            max_length=100,
            choices=FEES_CHOICES,
            blank=True)
    fees_amount = models.DecimalField(max_digits= 8, decimal_places=2)
    goods_and_services = models.BooleanField(default=False)
    goods_and_services_value = models.DecimalField(max_digits= 8, decimal_places=2)
    note = models.TextField(blank=True)




    # def save(self, *args, **kwargs):
    #     self.Account =
    #     when Company:
    #         Account = Company
    #     else Last_Name:
    #         if Last_Name2:
    #             if Last_Name == Last_Name2:
    #                 Account = [Last_Name + ", " + First_Name + " & " + First_Name2]
    #             else:
    #                 Account = [Last_Name + ", " + First_Name + " & " + Last_Name2 + ", " + First_Name2]
    #         else:
    #              Account = (Last_Name + ", " + First_Name)
    #              )
    #     super(Foo, self).save(*args, **kwargs) # Call the "real" save() method.




class Format(models.Model):
    FORMAT_CHOICES = (
        ('business', 'Business'),
        ('individual','Individual'),
        ('couple', 'Couple'),
        ('other', 'Other'),
    )
    Format = models.CharField(
        max_length=20,
        choices=FORMAT_CHOICES,
        default='Other',
    )

# Base contact model. All fields in all forms
# class Contact_old(models.Model):
#     Owner = models.ForeignKey(User, on_delete = models.CASCADE)
#     uuid = ShortUUIDField(unique=True, primary_key = True,)
#     Created_On = models.DateField(auto_now_add=True)
#     Note = models.TextField(blank=True)
#     Account = models.CharField(max_length=50)
#
#     Title = models.CharField(max_length=10, blank=True )
#     First_Name = models.CharField(max_length=30, blank=True )
#     Last_Name = models.CharField(max_length=30, blank=True )
#     Phone = models.CharField(max_length=20, blank=True )
#     Email = models.EmailField(validators=[validate_email], blank=True )
#
#     address = models.CharField(max_length=255, blank=True)
#     city = models.CharField(max_length=255,blank=True)
#     state = models.CharField(max_length=2,blank=True)
#     postal_code = models.CharField(max_length=20,blank=True)
#     country = models.CharField(max_length=30, default='USA', blank=True )
#

# class Individual(models.Model):
#         Donor = models.OneToOneField(
#         Contact,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#         Format = 'individual'
#         Title = models.CharField(max_length=10, blank=True )
#         First_Name = models.CharField(max_length=30, blank=False)
#         Last_Name = models.CharField(max_length=30, blank=False )
#         Phone = models.CharField(max_length=20, blank=True )
#         Email = models.EmailField(validators=[validate_email], blank=True )
#
#         address = models.CharField(max_length=255, blank=True)
#         city = models.CharField(max_length=255,blank=True)
#         state = models.CharField(max_length=2,blank=True)
#         postal_code = models.CharField(max_length=20,blank=True)
#         country = models.CharField(max_length=30, default='USA', blank=True )
#
#         def clean(self):
#         if not self.email or not (self.address & self.postal_code):
#             raise ValidationError("You must specify either email or telephone")
#
#
#
#         # Account = models.CharField(max_length=50)
#         # def __str__(self):
#         #     if Last_Name is None:
#         #         Account = Contact.objects.get(pk=uuid)
#         #     else:
#         #         Account = [Last_Name + ", " + First_Name]
#         #     return Account
#
#         @property
#         def full_name(self):
#             return u'%s %s' % (self.First_Name1, self.Last_Name1)
#
#         def __unicode__(self):
#             return u'%s' % self.full_name
#
# # For formset with multiple individuals
# class Spouse(models.Model):
#     Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
#     Format = 'couple'
#     SUBCATEGORY_CHOICES =(
#             ('member', 'Member'),
#             ('regular', 'Regular'),
#             ('first_time', 'First_Time'),
#             ('annual', 'Annual'),
#             ('otherdonor', 'Otherdonor'),
#             )
#     Subcategory = models.CharField(
#         max_length=20,
#         choices=SUBCATEGORY_CHOICES,
#         default='Otherdonor',
#         )
#     Title2 = models.CharField(max_length=10, blank=True )
#     First_Name2 = models.CharField(max_length=30, blank=True )
#     Last_Name2 = models.CharField(max_length=30, blank=True )
#     Email2 = models.EmailField(validators=[validate_email], blank=True )
#     Phone2 = models.CharField(max_length=20, blank=True )
#     Account = models.CharField(max_length=50)
#     def __str__(self):
#         if Last_Name is None:
#             Account = Contact.objects.get(pk=uuid)
#         elif Last_Name2 is None:
#             Account = (Last_Name + ", " + First_Name)
#         elif Last_Name == Last_Name2:
#             Account = [Last_Name + ", " + First_Name + " & " + First_Name2]
#         else:
#             Account = [Last_Name + ", " + First_Name + " & " + Last_Name2 + ", " + First_Name2]
#         return Account
#     @property
#     def couple(self):
#         return u'%s %s & %s %s' % (self.First_Name1, self.Last_Name1,
#             self.First_Name2, self.Last_Name2,)
#
#     def __unicode__(self):
#         return u'%s' % self.couple
#
# class Company_Donor(models.Model):
#     Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
#     Format = 'business'
#     SUBCATEGORY_CHOICES =(
#             ('regular', 'Regular'),
#             ('first_time', 'First_Time'),
#             ('annual', 'Annual'),
#             ('grant', 'Grant'),
#             ('otherdonor', 'Otherdonor'),
#             )
#     Subcategory = models.CharField(
#         max_length=20,
#         choices=SUBCATEGORY_CHOICES,
#         default='Otherdonor',
#         )
#     Company_Name = models.CharField(max_length=50)
#     Account = models.CharField(max_length=50, default = Company_Name)
#
# class Company_Vendor(models.Model):
#     Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
#     Format = 'business'
#     SUBCATEGORY_CHOICES =(
#             ('biller', 'Biller'),
#             ('contractor', 'Contractor'),
#             ('seller', 'Seller'),
#             ('othervendor', 'Othervendor'),
#             )
#     Subcategory = models.CharField(
#         max_length=20,
#         choices=SUBCATEGORY_CHOICES,
#         default='OtherDonor',
#         )
#     Company_Name = models.CharField(max_length=50,blank=True )
#     Account = models.CharField(max_length=50, default = User.username)
#
# #
# class Other(models.Model):
#     Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
#     Format = 'other'
#     Subcategory = 'other'
#     Company_Name = models.CharField(max_length=50)
#     Title2 = models.CharField(max_length=10, blank=True )
#     First_Name2 = models.CharField(max_length=30, blank=True )
#     Last_Name2 = models.CharField(max_length=30, blank=True )
#     Account = models.CharField(max_length=50)
#     def __str__(self):
#         if Company_Name:
#             Account = Company_Name
#         elif Last_Name:
#             Account = Last_Name
#         else:
#             Account = Contact
#         return Account
# #
# #
# # # Categories models
# # class Category(models.Model):
# #     CATEGORY_CHOICES = (('Donor', 'donor'),('Vendor', 'vendor'), ('Other', 'other'))
# #     Category = models.CharField(
# #         max_length=20,
# #         choices=CATEGORY_CHOICES,
# #         default='Other',
# #     )
# #
# class donor_categories(models.Model):
#     Category = 'donor'
#     CATEGORY_CHOICES = (
#     ('member', 'Member'),
#     ('regular', 'Regular'),
#     ('first_time', 'First_Time'),
#     ('annual', 'Annual'),
#     ('grant', 'Grant'),
#     ('otherdonor', 'Otherdonor')
#     )
#     Category = models.CharField(
#         max_length=20,
#         choices=CATEGORY_CHOICES,
#         default='otherdonor',
#     )
#     def get_absolute_url(self):
#         return u'/some_url/%d' % self.id
#
# class vendor_categories(models.Model):
#     Category = 'vendor'
#     SUBCATEGORY_CHOICES =(
#             ('biller', 'Biller'),
#             ('contractor', 'Contractor'),
#             ('seller', 'Seller'),
#             ('othervendor', 'Othervendor')
#             )
#     Subcategory = models.CharField(
#         max_length=20,
#         choices=SUBCATEGORY_CHOICES,
#         default='othervendor',
#         )
#     # def get_absolute_url(self):
#     #     return u'/some_url/%d' % self.id
#
# class other_categories(models.Model):
#     Category = 'other'
#     Subcategory = 'other'

    # def get_absolute_url(self):
    #     return u'/some_url/%d' % self.id



# # Allows for multiple addresses
# class Address(models.Model):
#     Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
#     address_type = models.CharField(max_length=10,blank=True)
#     address = models.CharField(max_length=255, blank=True)
#     city = models.CharField(max_length=255,blank=True)
#     state = models.CharField(max_length=2,blank=True)
#     postal_code = models.CharField(max_length=20,blank=True)
#     country = models.CharField(max_length=30, default='USA', blank=True )
