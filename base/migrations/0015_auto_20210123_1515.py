# Generated by Django 3.1.5 on 2021-01-23 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_audiopostcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiopost',
            name='thumbnail',
            field=models.ImageField(default='defaults/kobydrillsdotkom.png', upload_to='audio/%y/thumbnails/'),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='thumbnail',
            field=models.ImageField(blank=True, default='defaults/kobydrillsdotkom.png', null=True, upload_to='videos/%y/thumbnails/'),
        ),
    ]
