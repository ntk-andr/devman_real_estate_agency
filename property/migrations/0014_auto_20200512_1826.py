# Generated by Django 2.2.4 on 2020-05-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20200512_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='owner',
            options={'verbose_name': 'Собственника', 'verbose_name_plural': 'Собственники'},
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(related_name='apartments', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
