# Generated by Django 5.0 on 2023-12-20 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_gallarymodel_created_at_gallarymodel_updated_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GallaryModel',
        ),
    ]