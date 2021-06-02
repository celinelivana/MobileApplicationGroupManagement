# Generated by Django 3.1.7 on 2021-04-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('owner', models.CharField(max_length=100)),
                ('member', models.IntegerField(null=True)),
            ],
        ),
    ]