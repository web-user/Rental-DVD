# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentaldvd', '0006_auto_20181018_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='date_returned',
            field=models.DateTimeField(null=True),
        ),
    ]
