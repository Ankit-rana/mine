# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node_informer', '0003_auto_20150422_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='metadata',
            field=models.CharField(default=None, max_length=800),
        ),
        migrations.AlterField(
            model_name='node',
            name='policy',
            field=models.CharField(default=None, max_length=800),
        ),
        migrations.AlterField(
            model_name='node',
            name='state',
            field=models.CharField(default=None, max_length=600),
        ),
        migrations.AlterField(
            model_name='node',
            name='tags',
            field=models.CharField(default=None, max_length=600),
        ),
    ]
