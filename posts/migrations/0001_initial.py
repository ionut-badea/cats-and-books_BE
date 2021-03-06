# Generated by Django 2.2.7 on 2019-11-28 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('category', models.CharField(max_length=50, verbose_name='category')),
                ('slug', models.SlugField(default='slug', max_length=100, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'default_related_name': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='cover')),
                ('abstract', models.TextField(blank=True, max_length=300, null=True, verbose_name='abstract')),
                ('body', models.TextField(verbose_name='body')),
                ('draft', models.BooleanField(default=True, verbose_name='draft')),
                ('published', models.DateTimeField(blank=True, null=True, verbose_name='published')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to='posts.Category')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'default_related_name': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('tag', models.CharField(max_length=25, verbose_name='tag')),
                ('slug', models.SlugField(max_length=20, verbose_name='slug')),
                ('post', models.ManyToManyField(blank=True, related_name='tags', to='posts.Post')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'default_related_name': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('comment', models.TextField(verbose_name='comment')),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.Post')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'default_related_name': 'comments',
            },
        ),
    ]
