# Generated by Django 2.2.7 on 2019-12-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20191220_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images/articles', verbose_name='cover'),
        ),
    ]
