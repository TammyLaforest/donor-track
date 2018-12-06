# Generated by Django 2.1.4 on 2018-12-06 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositSlip',
            fields=[
                ('deposit_number', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('deposit_date', models.DateField(auto_now_add=True)),
                ('bank_account', models.CharField(choices=[('checking_account', 'Checking_Account'), ('savings_account', 'Savings_Account')], default='Checking_Account', max_length=100)),
                ('total_fees', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_income', models.DecimalField(decimal_places=2, max_digits=8)),
                ('net_deposit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cash_back', models.DecimalField(decimal_places=2, max_digits=8)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('payment_number', models.AutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('payment_method', models.CharField(choices=[('cash', 'Cash'), ('credit', 'Credit'), ('check', 'Check'), ('paypal', 'PayPal'), ('other_payment', 'Other_Payment')], default='Check', max_length=100)),
                ('payment_reference', models.CharField(blank=True, max_length=255)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('fees_source', models.CharField(blank=True, choices=[('paypal_fees', '{PayPal_Fees}'), ('credit_fee', 'Credit_Fee'), ('service_fee', 'Service_Fee'), ('bank_fee', 'Bank_Fee'), ('other_fee', 'Other_Payment')], max_length=100)),
                ('fees_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('goods_and_services', models.BooleanField(default=False)),
                ('goods_and_services_value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('note', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pledges',
            fields=[
                ('pledge_number', models.AutoField(primary_key=True, serialize=False)),
                ('pledge_date', models.DateField(auto_now_add=True)),
                ('pledge_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('income_category', models.CharField(choices=[('donation', 'Donation'), ('grant', 'Grant'), ('fundraiser', 'Fundraiser'), ('product', 'Product'), ('other_income', 'Other_Income')], default='Donation', max_length=100)),
                ('note', models.TextField(blank=True)),
                ('pledge_balance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payments_applied', models.DecimalField(decimal_places=2, max_digits=8)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Contact')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='payments',
            name='apply_payment_to',
            field=models.ManyToManyField(to='easydonorapp.Pledges'),
        ),
        migrations.AddField(
            model_name='payments',
            name='deposit_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easydonorapp.DepositSlip'),
        ),
        migrations.AddField(
            model_name='payments',
            name='donor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='payments',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
