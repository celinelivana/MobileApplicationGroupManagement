# Generated by Django 3.1.7 on 2021-05-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0027_group_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupid', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
