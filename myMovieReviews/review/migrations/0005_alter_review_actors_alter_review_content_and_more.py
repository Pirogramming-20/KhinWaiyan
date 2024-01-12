# Generated by Django 4.2.9 on 2024-01-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_alter_review_actors_alter_review_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='actors',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='director',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='image_url',
            field=models.URLField(default='https://picsum.photos/200/300'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='review',
            name='running_time',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='year',
            field=models.IntegerField(),
        ),
    ]
