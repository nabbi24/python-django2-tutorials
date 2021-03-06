# Generated by Django 2.0 on 2017-12-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loaders', '0009_auto_20171211_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='agency',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='commissionform',
            name='question_text',
        ),
        migrations.AddField(
            model_name='agency',
            name='agency_id',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='agency',
            name='areas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='commissionform',
            name='form_id',
            field=models.CharField(default='', max_length=8),
        ),
    ]
