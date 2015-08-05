# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node_informer', '0004_auto_20150422_0706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='dhcp_mac',
        ),
        migrations.RemoveField(
            model_name='node',
            name='facts',
        ),
        migrations.RemoveField(
            model_name='node',
            name='hostname',
        ),
        migrations.RemoveField(
            model_name='node',
            name='hw_info',
        ),
        migrations.RemoveField(
            model_name='node',
            name='last_checkin',
        ),
        migrations.RemoveField(
            model_name='node',
            name='log',
        ),
        migrations.RemoveField(
            model_name='node',
            name='metadata',
        ),
        migrations.RemoveField(
            model_name='node',
            name='node_id',
        ),
        migrations.RemoveField(
            model_name='node',
            name='node_name',
        ),
        migrations.RemoveField(
            model_name='node',
            name='node_spec',
        ),
        migrations.RemoveField(
            model_name='node',
            name='policy',
        ),
        migrations.RemoveField(
            model_name='node',
            name='root_password',
        ),
        migrations.RemoveField(
            model_name='node',
            name='state',
        ),
        migrations.RemoveField(
            model_name='node',
            name='tags',
        ),
        migrations.AddField(
            model_name='node',
            name='node',
            field=models.CharField(default=None, max_length=5000),
        ),
    ]
