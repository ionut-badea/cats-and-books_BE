# Generated by Django 3.0.3 on 2020-02-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0030_auto_20200220_1237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'default_related_name': 'articles', 'ordering': ['-published', 'title'], 'verbose_name': 'article', 'verbose_name_plural': 'articles'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'default_related_name': 'categories', 'ordering': ['name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'default_related_name': 'comments', 'ordering': ['-updated'], 'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'default_related_name': 'tags', 'ordering': ['name'], 'verbose_name': 'tag', 'verbose_name_plural': 'tags'},
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=150, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150, unique=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=25, unique=True, verbose_name='tag'),
        ),
    ]
