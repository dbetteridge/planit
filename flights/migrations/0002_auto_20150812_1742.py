# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='ArrivalDate',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Carrier',
        ),
    ]
