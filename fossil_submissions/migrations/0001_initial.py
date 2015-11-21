# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fossil_submissions.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('image', models.ImageField(max_length=1000, null=True, upload_to=fossil_submissions.models.picture_upload_to, blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
