# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fossil_submissions', '0003_appraisal'),
    ]

    operations = [
        migrations.AddField(
            model_name='appraisal',
            name='is_fossil',
            field=models.CharField(default=b'Maybe', max_length=100, choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Maybe', b'Maybe')]),
        ),
    ]
