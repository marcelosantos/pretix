# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-07 09:35
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pretixbase', '0036_auto_20160902_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankImportJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(choices=[('running', 'pending'), ('running', 'running'), ('error', 'error'), ('completed', 'completed')], default='running', max_length=32)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pretixbase.Event')),
            ],
        ),
        migrations.CreateModel(
            name='BankTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('imported', 'imported, unchecked'), ('nomatch', 'no match'), ('invalid', 'not valid'), ('error', 'error'), ('valid', 'valid'), ('already', 'valid, already paid'), ('discarded', 'manually discarded')], default='imported', max_length=32)),
                ('message', models.TextField()),
                ('checksum', models.CharField(db_index=True, max_length=190)),
                ('payer', models.TextField(blank=True)),
                ('reference', models.TextField(blank=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pretixbase.Event')),
                ('import_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banktransfer.BankImportJob')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pretixbase.Order')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='banktransaction',
            unique_together=set([('event', 'checksum')]),
        ),
    ]