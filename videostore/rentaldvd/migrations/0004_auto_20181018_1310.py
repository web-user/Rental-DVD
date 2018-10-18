# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentaldvd', '0003_rent_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='rent',
            field=models.ForeignKey(blank=True, default=None, to='rentaldvd.Rent'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='date_took',
            field=models.DateTimeField(blank=True),
        ),
    ]
