from django.db import models
from django.conf import settings

from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email
from django.forms import ModelForm

from django.contrib.auth import get_user_model
User = get_user_model()
from contacts.models import Contact
from model_utils import Choices


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

class Pledges(models.Model):
    owner = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )
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
    owner = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )
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
    owner = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )
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
