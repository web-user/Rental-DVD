# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentaldvd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('status', models.CharField(max_length=10, default='took', choices=[('took', 'Took the disk'), ('returned', 'Returned disk')])),
                ('date_took', models.DateTimeField(auto_now_add=True)),
                ('date_returned', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='dvd',
            name='rent',
            field=models.ForeignKey(default=None, to='rentaldvd.Rent'),
        ),
    ]
