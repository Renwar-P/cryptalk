# Generated by Django 3.2.23 on 2024-03-05 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_authorimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cointype',
            name='max_cap',
            field=models.TextField(blank=True),
        ),
    ]
