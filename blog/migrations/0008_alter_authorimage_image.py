# Generated by Django 3.2.23 on 2024-01-27 17:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_author_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorimage',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
