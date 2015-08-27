# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=50)),
                ('server_purpose', models.CharField(max_length=200, verbose_name='server purpose')),
                ('server_ip', models.GenericIPAddressField(verbose_name='ip address')),
                ('added', models.DateTimeField(verbose_name='date added')),
                ('server_level', models.CharField(max_length=4, choices=[('PROD', 'Production'), ('STAGE', 'Staging'), ('TEST', 'Test'), ('DEV', 'Development')], default='PROD')),
                ('server_type', models.CharField(max_length=3, choices=[('DB', 'Database'), ('WEB', 'Web')], default='WEB')),
                ('server_os', models.CharField(max_length=5, choices=[('WIN', 'Windows'), ('LINUX', 'Linux')], default='WIN')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('service_purpose', models.CharField(max_length=200, verbose_name='server purpose')),
                ('added', models.DateTimeField(verbose_name='date added')),
                ('servers', models.ManyToManyField(to='apps.Server')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='skills',
            field=models.ManyToManyField(to='apps.Skill'),
        ),
        migrations.AddField(
            model_name='app',
            name='services',
            field=models.ManyToManyField(to='apps.Service'),
        ),
    ]
