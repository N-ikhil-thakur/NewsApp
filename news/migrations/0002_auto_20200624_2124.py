# Generated by Django 3.0.7 on 2020-06-24 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsTypes',
            new_name='NewsType',
        ),
    ]