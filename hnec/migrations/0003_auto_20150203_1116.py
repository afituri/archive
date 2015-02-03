# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hnec', '0002_auto_20150121_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='desc',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
