# Generated by Django 2.2.7 on 2020-01-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20200115_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='nonnybadea@gmail.com', max_length=254, verbose_name='email'),
        ),
    ]
