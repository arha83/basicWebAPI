# Generated by Django 4.0.4 on 2022-08-27 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_var_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='var',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.vargroup'),
        ),
    ]
