# Generated by Django 5.0 on 2023-12-21 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_menumodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='price',
            field=models.FloatField(),
        ),
    ]
