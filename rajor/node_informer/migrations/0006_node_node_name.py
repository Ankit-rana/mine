# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node_informer', '0005_auto_20150422_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='node_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
