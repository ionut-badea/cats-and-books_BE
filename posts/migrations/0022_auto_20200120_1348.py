# Generated by Django 2.2.7 on 2020-01-20 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_auto_20200120_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='display',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated',
        ),
    ]
