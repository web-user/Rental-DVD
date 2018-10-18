# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rentaldvd', '0005_auto_20181018_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='user',
        ),
        migrations.RemoveField(
            model_name='dvd',
            name='rent',
        ),
        migrations.AddField(
            model_name='dvd',
            name='date_returned',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AddField(
            model_name='dvd',
            name='date_took',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='dvd',
            name='status',
            field=models.CharField(max_length=10, default='returned', choices=[('took', 'Took the disk'), ('returned', 'Returned disk')]),
        ),
        migrations.AddField(
            model_name='dvd',
            name='user',
            field=models.ForeignKey(blank=True, null=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Rent',
        ),
    ]
