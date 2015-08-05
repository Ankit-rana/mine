# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node_informer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_name', models.CharField(max_length=200)),
                ('node_spec', models.CharField(max_length=200)),
                ('node_id', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_ip', models.CharField(max_length=400)),
                ('server_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Servers',
        ),
        migrations.AddField(
            model_name='node',
            name='server',
            field=models.ForeignKey(to='node_informer.Server'),
        ),
    ]
