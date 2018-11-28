from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email

class Contact(models.Model):

    Owner = models.ForeignKey(User, on_delete = models.CASCADE)
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
        ('Company', 'Company'),
        ('individual', 'Individual'),
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


    # @models.permalink
    # def get_absolute_url(self):
    #     return 'contact_detail', [self.uuid]
    #
    # @models.permalink
    # def get_update_url(self):
    #     return 'contact_update', [self.uuid]
    #
    # @models.permalink
    # def get_delete_url(self):
    #     return 'contact_delete', [self.id]
