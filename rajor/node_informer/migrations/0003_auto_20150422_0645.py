# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node_informer', '0002_auto_20150420_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='dhcp_mac',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='node',
            name='facts',
            field=models.CharField(default=None, max_length=1200),
        ),
        migrations.AddField(
            model_name='node',
            name='hostname',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='node',
            name='hw_info',
            field=models.CharField(default=None, max_length=400),
        ),
        migrations.AddField(
            model_name='node',
            name='last_checkin',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='node',
            name='log',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='node',
            name='metadata',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='node',
            name='policy',
            field=models.CharField(default=None, max_length=600),
        ),
        migrations.AddField(
            model_name='node',
            name='root_password',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='node',
            name='state',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='node',
            name='tags',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
