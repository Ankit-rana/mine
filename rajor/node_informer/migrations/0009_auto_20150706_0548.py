# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node_informer', '0008_dummy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dummy',
            options={'permissions': (('view_console', 'can see console'), ('view_metadata', 'can view and edit metadata'), ('view_server', 'can view server'), ('view_node', "can view server's node"))},
        ),
    ]
