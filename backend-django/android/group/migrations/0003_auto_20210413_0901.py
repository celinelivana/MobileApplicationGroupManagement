# Generated by Django 3.1.7 on 2021-04-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_auto_20210413_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='requirements',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='group',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
