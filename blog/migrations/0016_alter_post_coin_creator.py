# Generated by Django 3.2.23 on 2024-04-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_coin_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='coin_creator',
            field=models.TextField(blank=True, null=True),
        ),
    ]