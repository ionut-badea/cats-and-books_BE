# Generated by Django 3.0.3 on 2020-03-12 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0040_auto_20200312_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='name'),
        ),
    ]
