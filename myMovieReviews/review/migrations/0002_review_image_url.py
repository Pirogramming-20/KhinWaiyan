# Generated by Django 4.2.9 on 2024-01-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image_url',
            field=models.URLField(default='https://picsum.photos/200/300'),
        ),
    ]
