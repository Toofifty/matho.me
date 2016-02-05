# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('built_with', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('src', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=50)),
            ],
        ),
    ]
