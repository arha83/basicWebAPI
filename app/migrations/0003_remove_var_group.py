# Generated by Django 4.0.4 on 2022-08-27 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_vargroup_var_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='var',
            name='group',
        ),
    ]
