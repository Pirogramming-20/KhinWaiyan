# Generated by Django 4.2.9 on 2024-01-17 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devtool', '0001_initial'),
        ('ideas', '0006_alter_idea_devtool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='devtool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devtool.devtool', verbose_name='예상 개발 툴'),
        ),
    ]