# Generated by Django 3.1.7 on 2021-04-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0016_auto_20210418_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='userid',
            field=models.IntegerField(blank=True),
        ),
    ]
