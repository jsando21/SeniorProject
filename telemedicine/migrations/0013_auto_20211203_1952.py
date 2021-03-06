# Generated by Django 3.2.7 on 2021-12-04 00:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telemedicine', '0012_auto_20211203_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartreports',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 3, 19, 52, 40, 601585)),
        ),
        migrations.AlterField(
            model_name='patients',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
