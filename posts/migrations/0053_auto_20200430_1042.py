# Generated by Django 3.0.4 on 2020-04-30 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0052_article_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateTimeField(blank=True, null=True, verbose_name='published'),
        ),
    ]
