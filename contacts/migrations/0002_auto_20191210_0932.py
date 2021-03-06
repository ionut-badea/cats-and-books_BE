# Generated by Django 2.2.7 on 2019-12-10 07:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('email', models.CharField(max_length=200, verbose_name='email')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('body', models.TextField(verbose_name='body')),
                ('reply', models.BooleanField(default=False, verbose_name='reply')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
