# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fossil_submissions', '0002_auto_20151122_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appraisal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('appraiser', models.ForeignKey(related_name='user_appraisals', to=settings.AUTH_USER_MODEL)),
                ('submission', models.ForeignKey(related_name='submission_appraisals', to='fossil_submissions.Submission')),
            ],
        ),
    ]
