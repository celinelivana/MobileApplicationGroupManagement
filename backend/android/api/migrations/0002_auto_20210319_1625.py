# Generated by Django 3.1.7 on 2021-03-19 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='users',
            name='access',
        ),
        migrations.RemoveField(
            model_name='users',
            name='nationality',
        ),
    ]
