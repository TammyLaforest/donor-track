from django.db import models
from django import forms

from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email
from django.forms import ModelForm

from django.contrib.auth import get_user_model
User = get_user_model()

# Only logged in user can see their own contacts in list
# http://www.effectivedjango.com/tutorial/authzn.html

class Category(models.Model):
    CATEGORY_CHOICES = (('Donor', 'donor'),('Vendor', 'vendor'), ('Other', 'other'))
    Category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Other',
    )

class Subcategory(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    SUBCATEGORY_CHOICES =(
            ('member', 'Member'),
            ('regular', 'Regular'),
            ('first_time', 'First_Time'),
            ('annual', 'Annual'),
            ('grant', 'Grant'),
            ('otherdonor', 'Otherdonor'),

            ('biller', 'Biller'),
            ('contractor', 'Contractor'),
            ('seller', 'Seller'),

            ('other', 'Other'),
            )
    Subcategory = models.CharField(
        max_length=20,
        choices=SUBCATEGORY_CHOICES,
        default='Other',
        )
#
# class Person(models.Model):
#     name = models.CharField(max_length=100)
#     birthdate = models.DateField(null=True, blank=True)
#     country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
#     city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
#

class Contact(models.Model):

    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):

        return ' '.join([
            self.id,
            self.username,
        ])

    def get_absolute_url(self):

        return reverse('contacts-view', kwargs={'pk': self.id})

    uuid = ShortUUIDField(unique=True, primary_key = True,)
    Created_On = models.DateField(auto_now_add=True)

    CATEGORY_CHOICES = (
    ('Donor', (
            ('member', 'Member'),
            ('regular', 'Regular'),
            ('first_time', 'First_Time'),
            ('annual', 'Annual'),
            ('grant', 'Grant'),
            ('otherdonor', 'Otherdonor'),
        )
    ),
    ('Vendor', (
            ('biller', 'Biller'),
            ('contractor', 'Contractor'),
            ('seller', 'Seller'),
        )
    ),
    ('unknown', 'Unknown'),
    ('other', 'Other'),

    )

    Category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Unknown',
    )
    FORMAT_CHOICES = (
        ('company', 'Company'),
        ('individual','Individual'),
        ('couple', 'Couple'),
        ('other', 'Other'),
    )

    Contact_Format = models.CharField(
        max_length=20,
        choices=FORMAT_CHOICES,
        default='Other',
    )

    Company = models.CharField(max_length=50,blank=True )
    First_Name1 = models.CharField(max_length=30, blank=True )
    Last_Name1 = models.CharField(max_length=30, blank=True )
    First_Name2 = models.CharField(max_length=30, blank=True )
    Last_Name2 = models.CharField(max_length=30, blank=True )
    Address_Number = models.CharField(max_length=20, blank=True )
    Address_Street = models.CharField(max_length=30, blank=True )
    Address_Street2 = models.CharField(max_length=30, blank=True )
    Address_City = models.CharField(max_length=30, blank=True )
    Address_State = models.CharField(max_length=30, blank=True )
    Address_Postal_Code = models.CharField(max_length=30, blank=True )
    Address_Country = models.CharField(max_length=30, default='USA', blank=True )
    Phone1 = models.CharField(max_length=20, blank=True )
    Phone2 = models.CharField(max_length=20, blank=True )
    Email1 = models.EmailField(validators=[validate_email], blank=True )
    Email2 = models.EmailField(validators=[validate_email], blank=True )
    Note = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Contacts'



    @property
    def full_name(self):
        return u'%s %s' % (self.First_Name1, self.Last_Name1)

    def __unicode__(self):
        return u'%s' % self.full_name


    @property
    def couple(self):
        return u'%s %s & %s %s' % (self.First_Name1, self.Last_Name1,
            self.First_Name2, self.Last_Name2,)

    def __unicode__(self):
        return u'%s' % self.couple

    def __unicode__(self):
        return u'%s' % self.Company

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class Select_ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    # if category.lower() == donor:
    #     if Contact_Format.lower() == company:
    #         fields = ['Company', 'First_Name1', 'Last_Name1', 'Address_Number', 'Address_Street', 'Address_Street2', 'Address_City', 'Address_State', 'Address_Postal_Code', 'Address_Country', 'Phone1', 'Email1', 'Note']
    #     elif Contact_Format.lower() == individual:
    #         fields = ['First_Name1', 'Last_Name1', 'Address_Number', 'Address_Street', 'Address_Street2', 'Address_City', 'Address_State', 'Address_Postal_Code', 'Address_Country', 'Phone1', 'Email1', 'Note']
    #     elif Contact_Format.lower() == couple:
    #         fields = ['First_Name1', 'Last_Name1', 'First_Name2', 'Last_Name2','Address_Number', 'Address_Street', 'Address_Street2', 'Address_City', 'Address_State', 'Address_Postal_Code', 'Address_Country', 'Phone1', 'Email1', 'Phone2', 'Email2', 'Note']
    #     else:
    #         fields ='__all__'
    # if category.lower() == vendor:
    #     fields = ['Company', 'First_Name1', 'Last_Name1', 'Address_Number', 'Address_Street', 'Address_Street2', 'Address_City', 'Address_State', 'Address_Postal_Code', 'Address_Country', 'Phone1', 'Email1', 'Note']
    # else:
        # fields ='__all__'


def __init__(self, *args, **kwargs):
    is_staff = kwargs.pop('is_staff')
    super(AddMovementForm, self).__init__(*args, **kwargs)
    if is_staff:
        self.fields['status'].choices = STAFF_STATUS_CHOICES
    else:
        self.fields['status'].choices = STATUS_CHOICES




class Donor(models.Model):
    Owner = User
    uuid = ShortUUIDField(unique=True, primary_key = True,)
    Created_On = models.DateField(auto_now_add=True)

    Category = 'donor'

    SUBCATEGORY_CHOICES =(
            ('member', 'Member'),
            ('regular', 'Regular'),
            ('first_time', 'First_Time'),
            ('annual', 'Annual'),
            ('grant', 'Grant'),
            ('otherdonor', 'Otherdonor'),
            )
    Subcategory = models.CharField(
        max_length=20,
        choices=SUBCATEGORY_CHOICES,
        default='Other',
        )

    FORMAT_CHOICES = (
        ('company', 'Company'),
        ('individual','Individual'),
        ('couple', 'Couple'),
        ('other', 'Other'),
    )

    Contact_Format = models.CharField(
        max_length=20,
        choices=FORMAT_CHOICES,
        default='Other',
    )

    Company = models.CharField(max_length=50,blank=True )
    First_Name1 = models.CharField(max_length=30, blank=True )
    Last_Name1 = models.CharField(max_length=30, blank=True )
    First_Name2 = models.CharField(max_length=30, blank=True )
    Last_Name2 = models.CharField(max_length=30, blank=True )
    Address_Number = models.CharField(max_length=20, blank=True )
    Address_Street = models.CharField(max_length=30, blank=True )
    Address_Street2 = models.CharField(max_length=30, blank=True )
    Address_City = models.CharField(max_length=30, blank=True )
    Address_State = models.CharField(max_length=30, blank=True )
    Address_Postal_Code = models.CharField(max_length=30, blank=True )
    Address_Country = models.CharField(max_length=30, default='USA', blank=True )
    Phone1 = models.CharField(max_length=20, blank=True )
    Phone2 = models.CharField(max_length=20, blank=True )
    Email1 = models.EmailField(validators=[validate_email], blank=True )
    Email2 = models.EmailField(validators=[validate_email], blank=True )
    Note = models.TextField(blank=True)


class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'

class VendorForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
