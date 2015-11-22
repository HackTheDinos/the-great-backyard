# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fossil_submissions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='approved',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Approved', b'Approved'), (b'Uncertain', b'Uncertain'), (b'Denied', b'Denied')]),
        ),
        migrations.AddField(
            model_name='submission',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
