# Generated by Django 3.0.8 on 2020-07-15 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200701_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 15, 12, 42, 725326)),
        ),
    ]