# Generated by Django 3.2.23 on 2024-04-07 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='coin_type',
        ),
        migrations.AddField(
            model_name='post',
            name='coin_type_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='coin_type_max_cap',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='coin_type_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='custom_coin_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='AuthorImage',
        ),
        migrations.DeleteModel(
            name='CoinType',
        ),
    ]
