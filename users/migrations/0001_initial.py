# Generated by Django 2.1.4 on 2018-12-06 02:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=150)),
                ('taxid', models.CharField(blank=True, max_length=50)),
                ('Phone', models.CharField(blank=True, max_length=50)),
                ('Address', models.CharField(blank=True, max_length=255)),
                ('City', models.CharField(blank=True, max_length=255)),
                ('State', models.CharField(blank=True, max_length=2)),
                ('Postal_code', models.CharField(blank=True, max_length=20)),
                ('Country', models.CharField(blank=True, default='USA', max_length=30)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='BusinessProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='e-mail address')),
                ('verified', models.BooleanField(default=False, verbose_name='verified')),
                ('primary', models.BooleanField(default=False, verbose_name='primary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Em_Ad_User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'email address',
                'verbose_name_plural': 'email addresses',
            },
        ),
        migrations.CreateModel(
            name='EmailConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('sent', models.DateTimeField(null=True, verbose_name='sent')),
                ('key', models.CharField(max_length=64, unique=True, verbose_name='key')),
                ('email_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Em_Ad_Conf', to='users.EmailAddress', verbose_name='e-mail address')),
            ],
            options={
                'verbose_name': 'email confirmation',
                'verbose_name_plural': 'email confirmations',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
