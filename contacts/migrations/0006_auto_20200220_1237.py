# Generated by Django 3.0.3 on 2020-02-20 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20200219_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='id',
            new_name='uid',
        ),
    ]
