# Generated by Django 3.2.23 on 2024-04-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_post_custom_coin_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='coin_creator',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]