# Generated by Django 2.2.4 on 2020-05-18 22:02

from django.db import migrations


def owner_and_flat(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    for owner in Owner.objects.all():
        flat = Flat.objects.get(id=owner.id)
        owner.flats.add(flat)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0013_auto_20200515_2015'),
    ]

    operations = [
        migrations.RunPython(owner_and_flat)
    ]