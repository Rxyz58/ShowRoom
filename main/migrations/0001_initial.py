# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-12 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address_city', models.CharField(max_length=30)),
                ('address_district', models.CharField(max_length=30)),
                ('contact', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('address_city', models.CharField(max_length=30)),
                ('address_district', models.CharField(max_length=30)),
                ('contact', models.BigIntegerField()),
                ('salary', models.IntegerField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('joined_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.employee')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('created_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.department'),
        ),
    ]
