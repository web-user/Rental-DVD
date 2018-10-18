# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rentaldvd', '0007_auto_20181018_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='date_returned',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='date_took',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
