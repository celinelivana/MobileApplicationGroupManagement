# Generated by Django 3.1.7 on 2021-03-19 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210319_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='student_id',
        ),
    ]
