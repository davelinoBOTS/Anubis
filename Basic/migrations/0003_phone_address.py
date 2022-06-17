# Generated by Django 4.0.5 on 2022-06-17 02:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('Basic', '0002_add_world'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Verbose ID')),
                ('registrationDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Verbose Registration Date')),
                ('updateDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Verbose Update Date')),
                ('isActive', models.BooleanField(default=True, verbose_name='Verbose Is Active')),
                ('ddd', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(2)], verbose_name='Verbose DDD')),
                ('number', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(10)], verbose_name='Verbose Number')),
                ('extension', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.MaxLengthValidator(5)], verbose_name='Verbose Extension')),
                ('contact', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MaxLengthValidator(100)], verbose_name='Verbose Contact')),
                ('typePhone', models.CharField(choices=[('HOME', 'Home'), ('WORK', 'Work'), ('FAMILY', 'Family'), ('MOBILE', 'Mobile'), ('FAX', 'Fax'), ('OUTHERS', 'Outhers')], max_length=100, verbose_name='Verbose Type Phone')),
            ],
            options={
                'verbose_name': 'Verbose Phone',
                'verbose_name_plural': 'Verbose Phone Plural',
                'ordering': ['ddd'],
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Verbose ID')),
                ('registrationDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Verbose Registration Date')),
                ('updateDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Verbose Update Date')),
                ('isActive', models.BooleanField(default=True, verbose_name='Verbose Is Active')),
                ('publicPlace', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(255)], verbose_name='Verbose Public Place')),
                ('number', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.MaxLengthValidator(5)], verbose_name='Verbose Number')),
                ('complement', models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.MaxLengthValidator(255)], verbose_name='Verbose Complement')),
                ('referencePoint', models.TextField(blank=True, null=True, verbose_name='Verbose Reference Point')),
                ('zipCode', localflavor.br.models.BRPostalCodeField(max_length=9, verbose_name='Verbose Zip Code')),
                ('typeAddress', models.CharField(choices=[('HOME', 'Home'), ('WORK', 'Work'), ('FAMILY', 'Family'), ('OUTHERS', 'Outhers')], max_length=100, verbose_name='Verbose Type Address')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Basic.neighborhood', verbose_name='Verbose Neighborhood')),
            ],
            options={
                'verbose_name': 'Verbose Address',
                'verbose_name_plural': 'Verbose Address Plural',
                'ordering': ['publicPlace', 'zipCode', 'typeAddress'],
            },
        ),
    ]
