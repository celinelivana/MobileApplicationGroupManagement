# Generated by Django 3.1.7 on 2021-04-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0026_requests_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='tags',
            field=models.JSONField(null=True),
        ),
    ]
