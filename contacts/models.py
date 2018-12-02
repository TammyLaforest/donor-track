from django.db import models
from django import forms

from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email
from django.forms import ModelForm

from django.contrib.auth.models import User

class Contact(models.Model):
    Owner = models.ForeignKey(User, on_delete = models.CASCADE)
    uuid = ShortUUIDField(unique=True, primary_key = True,)
    Created_On = models.DateField(auto_now_add=True)
    Note = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Contacts'

class Format(models.Model):
    Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
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

class Address(models.Model):
    Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    address_type = models.CharField(max_length=10,blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255,blank=True)
    state = models.CharField(max_length=2,blank=True)
    postal_code = models.CharField(max_length=20,blank=True)

class Email(models.Model):
    Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    Email1 = models.EmailField(validators=[validate_email], blank=True )
    Email2 = models.EmailField(validators=[validate_email], blank=True )

class Phone(models.Model):
    Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    Phone1 = models.CharField(max_length=20, blank=True )
    Phone2 = models.CharField(max_length=20, blank=True )

class Company_Vendor(models.Model):
    Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    Format = 'business'
    SUBCATEGORY_CHOICES =(
            ('biller', 'Biller'),
            ('contractor', 'Contractor'),
            ('seller', 'Seller'),
            ('othervendor', 'Othervendor'),
            )
    Subcategory = models.CharField(
        max_length=20,
        choices=SUBCATEGORY_CHOICES,
        default='OtherDonor',
        )
    Company_Name = models.CharField(max_length=50,blank=True )
    First_Name = models.CharField(max_length=30, blank=True )
    Last_Name = models.CharField(max_length=30, blank=True )
    Account = models.CharField(max_length=50, blank=False, default = User.username)
    # class Meta:
    #     unique_together = ('contact', 'Account')

class Company_Donor(models.Model):
    Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    Format = 'business'
    SUBCATEGORY_CHOICES =(
            ('regular', 'Regular'),
            ('first_time', 'First_Time'),
            ('annual', 'Annual'),
            ('grant', 'Grant'),
            ('otherdonor', 'Otherdonor'),
            )
    Subcategory = models.CharField(
        max_length=20,
        choices=SUBCATEGORY_CHOICES,
        default='Otherdonor',
        )
    Company_Name = models.CharField(max_length=50)
    First_Name1 = models.CharField(max_length=30, blank=True)
    Last_Name1 = models.CharField(max_length=30, blank=True)
    Account = models.CharField(max_length=50, default = Company_Name)
    # class Meta:
    #     unique_together = ('contact', 'Account')

class Individual(models.Model):
        Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
        Format = 'individual'
        SUBCATEGORY_CHOICES =(
                ('member', 'Member'),
                ('regular', 'Regular'),
                ('first_time', 'First_Time'),
                ('annual', 'Annual'),
                ('otherdonor', 'Otherdonor'),
                )
        Subcategory = models.CharField(
            max_length=20,
            choices=SUBCATEGORY_CHOICES,
            default='Otherdonor',
            )
        Title = models.CharField(max_length=10, blank=True )
        First_Name = models.CharField(max_length=30, blank=True )
        Last_Name = models.CharField(max_length=30, blank=True )
        Account = models.CharField(max_length=50)
        def __str__(self):
            if Last_Name is None:
                Account = Contact.objects.get(pk=uuid)
            else:
                Account = [Last_Name + ", " + First_Name]
            return Account
        # class Meta:
        #     unique_together = ('contact', 'Account')
        @property
        def full_name(self):
            return u'%s %s' % (self.First_Name1, self.Last_Name1)

        def __unicode__(self):
            return u'%s' % self.full_name

class Couple(models.Model):
    Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    Format = 'couple'
    SUBCATEGORY_CHOICES =(
            ('member', 'Member'),
            ('regular', 'Regular'),
            ('first_time', 'First_Time'),
            ('annual', 'Annual'),
            ('otherdonor', 'Otherdonor'),
            )
    Subcategory = models.CharField(
        max_length=20,
        choices=SUBCATEGORY_CHOICES,
        default='OtherDonor',
        )
    Title = models.CharField(max_length=10, blank=True )
    First_Name = models.CharField(max_length=30, blank=True )
    Last_Name = models.CharField(max_length=30, blank=True )
    Title2 = models.CharField(max_length=10, blank=True )
    First_Name2 = models.CharField(max_length=30, blank=True )
    Last_Name2 = models.CharField(max_length=30, blank=True )
    Account = models.CharField(max_length=50)
    def __str__(self):
        if Last_Name is None:
            Account = Contact.objects.get(pk=uuid)
        elif Last_Name2 is None:
            Account = (Last_Name + ", " + First_Name)
        elif Last_Name == Last_Name2:
            Account = [Last_Name + ", " + First_Name + " & " + First_Name2]
        else:
            Account = [Last_Name + ", " + First_Name + " & " + Last_Name2 + ", " + First_Name2]
        return Account
    # class Meta:
    #     unique_together = ('contact', 'Account')

    @property
    def couple(self):
        return u'%s %s & %s %s' % (self.First_Name1, self.Last_Name1,
            self.First_Name2, self.Last_Name2,)

    def __unicode__(self):
        return u'%s' % self.couple

class Other(models.Model):
    Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    Format = 'other'
    Subcategory = 'other'
    Title = models.CharField(max_length=10, blank=True )
    First_Name = models.CharField(max_length=30, blank=True )
    Last_Name = models.CharField(max_length=30, blank=True )
    Title2 = models.CharField(max_length=10, blank=True )
    First_Name2 = models.CharField(max_length=30, blank=True )
    Last_Name2 = models.CharField(max_length=30, blank=True )
    Account = models.CharField(max_length=50)
    def __str__(self):
        if Last_Name:
            Account = Last_Name
        elif Company_Name:
            Account = Company_Name
        else:
            Account = Contact
        return Account
    # class Meta:
    #     unique_together = ('contact', 'Account')

class Category(models.Model):
    CATEGORY_CHOICES = (('Donor', 'donor'),('Vendor', 'vendor'), ('Other', 'other'))
    Category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Other',
    )

class donor_categories(models.Model):
    Category = 'donor'
    CATEGORY_CHOICES = (
    ('member', 'Member'),
    ('regular', 'Regular'),
    ('first_time', 'First_Time'),
    ('annual', 'Annual'),
    ('grant', 'Grant'),
    ('otherdonor', 'Otherdonor')
    )
    Category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='otherdonor',
    )

class vendor_categories(models.Model):
    Category = 'vendor'
    SUBCATEGORY_CHOICES =(
            ('biller', 'Biller'),
            ('contractor', 'Contractor'),
            ('seller', 'Seller'),
            ('othervendor', 'Othervendor')
            )
    Subcategory = models.CharField(
        max_length=20,
        choices=SUBCATEGORY_CHOICES,
        default='othervendor',
        )

class other_categories(models.Model):
    Category = 'other'
    Subcategory = 'other'

# class Contact(models.Model):
#
#     Owner = models.ForeignKey(User, on_delete = models.CASCADE)
#     def __str__(self):
#         return ' '.join([
#             self.id,
#             self.username,
#         ])
#     def get_absolute_url(self):
#         return reverse('contacts_view', kwargs={'pk': self.id})
#
#     uuid = ShortUUIDField(unique=True, primary_key = True,)
#     Account = models.CharField(max_length=50, default = uuid)
#     Created_On = models.DateField(auto_now_add=True)
#
#     CATEGORY_CHOICES = (
#     ('Donor', (
#             ('member', 'Member'),
#             ('regular', 'Regular'),
#             ('first_time', 'First_Time'),
#             ('annual', 'Annual'),
#             ('grant', 'Grant'),
#             ('otherdonor', 'Otherdonor'),
#         )
#     ),
#     ('Vendor', (
#             ('biller', 'Biller'),
#             ('contractor', 'Contractor'),
#             ('seller', 'Seller'),
#             ('othervendor', 'Othervendor'),
#         )
#     ),
#     ('othercontact', 'Othercontact'),
#     )
#
#     Category = models.CharField(
#         max_length=20,
#         choices=CATEGORY_CHOICES,
#         default='othercontact',
#     )


    # Company = models.CharField(max_length=50,blank=True )
    # First_Name1 = models.CharField(max_length=30, blank=True )
    # Last_Name1 = models.CharField(max_length=30, blank=True )
    # First_Name2 = models.CharField(max_length=30, blank=True )
    # Last_Name2 = models.CharField(max_length=30, blank=True )


#
#
# class Donor(models.Model):
#     Owner = models.ForeignKey(User, on_delete = models.CASCADE)
#     def __str__(self):
#         return ' '.join([
#             self.id,
#             self.username,
#         ])
#     def get_absolute_url(self):
#         return reverse('donors_view', kwargs={'pk': self.id})
#
#     uuid = ShortUUIDField(unique=True, primary_key = True,)
#
#     Created_On = models.DateField(auto_now_add=True)
#
#     Category = 'donor'
#
#     SUBCATEGORY_CHOICES =(
#             ('member', 'Member'),
#             ('regular', 'Regular'),
#             ('first_time', 'First_Time'),
#             ('annual', 'Annual'),
#             ('grant', 'Grant'),
#             ('otherdonor', 'Otherdonor'),
#             )
#     Subcategory = models.CharField(
#         max_length=20,
#         choices=SUBCATEGORY_CHOICES,
#         default='Other',
#         )
#
#     FORMAT_CHOICES = (
#         ('company', 'Company'),
#         ('individual','Individual'),
#         ('couple', 'Couple'),
#         ('other', 'Other'),
#     )
#
#     Contact_Format = models.CharField(
#         max_length=20,
#         choices=FORMAT_CHOICES,
#         default='Other',
#     )
#
#     Company = models.CharField(max_length=50,blank=True )
#     First_Name1 = models.CharField(max_length=30, blank=True )
#     Last_Name1 = models.CharField(max_length=30, blank=True )
#     First_Name2 = models.CharField(max_length=30, blank=True )
#     Last_Name2 = models.CharField(max_length=30, blank=True )
#     Address_Number = models.CharField(max_length=20, blank=True )
#     Address_Street = models.CharField(max_length=30, blank=True )
#     Address_Street2 = models.CharField(max_length=30, blank=True )
#     Address_City = models.CharField(max_length=30, blank=True )
#     Address_State = models.CharField(max_length=30, blank=True )
#     Address_Postal_Code = models.CharField(max_length=30, blank=True )
#     Address_Country = models.CharField(max_length=30, default='USA', blank=True )
#     Phone1 = models.CharField(max_length=20, blank=True )
#     Phone2 = models.CharField(max_length=20, blank=True )
#     Email1 = models.EmailField(validators=[validate_email], blank=True )
#     Email2 = models.EmailField(validators=[validate_email], blank=True )
#     Note = models.TextField(blank=True)
