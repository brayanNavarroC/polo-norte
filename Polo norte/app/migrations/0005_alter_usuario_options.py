# Generated by Django 5.0.2 on 2024-08-27 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_authgroup_delete_authgrouppermissions_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'managed': False},
        ),
    ]
