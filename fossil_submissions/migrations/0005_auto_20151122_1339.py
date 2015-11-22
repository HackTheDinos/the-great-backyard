# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fossil_submissions', '0004_appraisal_is_fossil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appraisal',
            name='submission',
            field=models.ForeignKey(related_name='submission_appraisals', to='fossil_submissions.Submission', unique=True),
        ),
    ]
