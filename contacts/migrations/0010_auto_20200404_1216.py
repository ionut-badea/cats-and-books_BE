# Generated by Django 3.0.4 on 2020-04-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_auto_20200324_1839'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'default_related_name': 'messages', 'get_latest_by': ['-created'], 'ordering': ['email'], 'verbose_name': 'message', 'verbose_name_plural': 'messages'},
        ),
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(max_length=500, verbose_name='message'),
        ),
    ]
