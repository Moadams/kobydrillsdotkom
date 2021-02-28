# Generated by Django 3.1.5 on 2021-01-23 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_auto_20210123_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiopost',
            name='thumbnail',
            field=models.ImageField(blank=True, default='defaults/kobydrillsdotkom.png', null=True, upload_to='audios/%y/thumbnails'),
        ),
        migrations.AddField(
            model_name='videopost',
            name='thumbnail',
            field=models.ImageField(blank=True, default='defaults/kobydrillsdotkom.png', null=True, upload_to='videos/%y/thumbnails'),
        ),
    ]
