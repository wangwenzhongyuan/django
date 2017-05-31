# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('user_passwd', models.CharField(max_length=40)),
                ('user_email', models.CharField(max_length=20)),
                ('user_tel', models.CharField(default=b'', max_length=20)),
                ('user_post', models.CharField(default=b'', max_length=20)),
                ('user_addr', models.CharField(default=b'', max_length=255)),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]
