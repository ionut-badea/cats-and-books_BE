# Generated by Django 3.0.3 on 2020-02-20 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_auto_20200220_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='id',
            new_name='uid',
        ),
    ]
