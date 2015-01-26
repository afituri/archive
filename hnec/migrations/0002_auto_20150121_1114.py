# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hnec', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='real_date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
