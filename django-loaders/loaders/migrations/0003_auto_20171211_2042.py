# Generated by Django 2.0 on 2017-12-11 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loaders', '0002_auto_20171211_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='commission_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loaders.CommissionForm'),
        ),
    ]
