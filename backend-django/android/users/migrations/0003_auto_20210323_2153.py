# Generated by Django 3.1.7 on 2021-03-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210323_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
