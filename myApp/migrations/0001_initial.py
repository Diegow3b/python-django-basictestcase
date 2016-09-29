# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atributo_string', models.CharField(max_length=50)),
                ('atributo_int', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Meu Modelo',
            },
        ),
    ]
