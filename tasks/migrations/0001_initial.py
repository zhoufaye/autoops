# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-06 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root', models.CharField(max_length=32, null=True, verbose_name='用户')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='IP')),
                ('port', models.CharField(max_length=32, null=True, verbose_name='端口')),
                ('cmd', models.CharField(max_length=128, null=True, verbose_name='命令')),
                ('user', models.CharField(max_length=32, null=True, verbose_name='操作者')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '历史命令',
                'verbose_name_plural': '历史命令',
                'db_table': 'history',
            },
        ),
    ]
