# Generated by Django 3.2.7 on 2021-11-15 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telemedicine', '0005_auto_20211114_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_patient',
        ),
    ]
