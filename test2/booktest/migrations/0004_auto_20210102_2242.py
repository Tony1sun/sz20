# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20201231_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeBasicInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=False)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('addr', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type_name', models.CharField(max_length=20)),
                ('type_news', models.ManyToManyField(to='booktest.NewsInfo')),
            ],
        ),
        migrations.AddField(
            model_name='newsinfo',
            name='news_type',
            field=models.ManyToManyField(to='booktest.NewsType'),
        ),
        migrations.AddField(
            model_name='employeebasicinfo',
            name='employee_basic',
            field=models.OneToOneField(to='booktest.EmployeeDetailInfo'),
        ),
    ]
