# Generated by Django 3.0.4 on 2020-04-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0053_auto_20200430_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='month',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='month'),
        ),
        migrations.AddField(
            model_name='article',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='year'),
        ),
    ]