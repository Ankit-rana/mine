# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node_informer', '0006_node_node_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='node',
            field=models.CharField(default=None, max_length=15000),
        ),
    ]
