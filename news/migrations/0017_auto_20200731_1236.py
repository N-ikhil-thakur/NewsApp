# Generated by Django 3.0.8 on 2020-07-31 06:51

import datetime
from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20200723_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developersinfo',
            name='notice',
            field=djrichtextfield.models.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 12, 36, 43, 609321)),
        ),
    ]
