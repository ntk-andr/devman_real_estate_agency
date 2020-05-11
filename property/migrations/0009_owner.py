# Generated by Django 2.2.4 on 2020-05-11 15:09

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20200511_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owner_phone_pure', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='RU', verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(related_name='flats_in_owner', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
            options={
                'verbose_name': 'Собвственника',
                'verbose_name_plural': 'Собственники',
            },
        ),
    ]
