# Generated by Django 3.1.7 on 2021-05-05 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_newuser_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='isTeacher',
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
    ]
