# Generated by Django 3.0.4 on 2020-04-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0048_auto_20200404_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='posts.Tag'),
        ),
    ]
