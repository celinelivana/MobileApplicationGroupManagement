# Generated by Django 3.1.7 on 2021-05-31 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210601_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='applied',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='likes',
            field=models.JSONField(default=list),
        ),
    ]
