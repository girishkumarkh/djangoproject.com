# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0009_djangohero_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangohero',
            name='url',
            field=models.URLField(verbose_name='URL', blank=True),
            preserve_default=True,
        ),
    ]
