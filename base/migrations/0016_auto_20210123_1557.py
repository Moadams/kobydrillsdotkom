# Generated by Django 3.1.5 on 2021-01-23 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20210123_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiopost',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='videopost',
            name='thumbnail',
        ),
    ]