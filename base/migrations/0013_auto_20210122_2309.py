# Generated by Django 3.1.5 on 2021-01-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20210122_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiopost',
            name='thumbnail',
            field=models.ImageField(default='defaults/headphone_audio.jpg', upload_to='audio/%y/thumbnails/'),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='thumbnail',
            field=models.ImageField(default='defaults/videos.jpg', upload_to='videos/%y/thumbnails/'),
        ),
    ]