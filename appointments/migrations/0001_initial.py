# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=500)),
                ('start_time', models.DateTimeField(verbose_name='Appointment Start')),
                ('end_time', models.DateTimeField(verbose_name='Appointment End')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='host',
            field=models.ForeignKey(to='appointments.Host'),
        ),
    ]
