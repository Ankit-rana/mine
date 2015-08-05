# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_ip', models.CharField(max_length=400)),
                ('node_name', models.CharField(max_length=200)),
                ('node_spec', models.CharField(max_length=200)),
                ('node_id', models.CharField(max_length=300)),
            ],
        ),
    ]
