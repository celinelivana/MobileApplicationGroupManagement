# Generated by Django 3.1.7 on 2021-04-15 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_group_applications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(blank=True, max_length=100)),
                ('groupname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='group.group')),
            ],
            options={
                'unique_together': {('groupname', 'userid')},
            },
        ),
    ]
