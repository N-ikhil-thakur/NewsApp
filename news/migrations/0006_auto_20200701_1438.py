# Generated by Django 3.0.8 on 2020-07-01 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200701_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='body',
        ),
        migrations.RemoveField(
            model_name='news',
            name='body_eng',
        ),
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(default='विवरण भेटिएन', verbose_name='विवरण'),
        ),
        migrations.AddField(
            model_name='news',
            name='description_eng',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='editor',
            field=models.CharField(default='सहयोगी समाचार', max_length=100, verbose_name='सम्पादक'),
        ),
        migrations.AlterField(
            model_name='news',
            name='editor_eng',
            field=models.CharField(default='Sahayogi News', max_length=100, verbose_name='Editor'),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 14, 38, 47, 592389)),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Titie'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_eng',
            field=models.CharField(max_length=250, null=True, verbose_name='शिर्षक'),
        ),
    ]