# Generated by Django 3.1.7 on 2021-04-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210324_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='bio',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='newuser',
            name='major',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
