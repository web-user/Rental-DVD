# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentaldvd', '0004_auto_20181018_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='rent',
            field=models.ForeignKey(blank=True, null=True, default=None, to='rentaldvd.Rent'),
        ),
    ]
