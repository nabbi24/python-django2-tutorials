# Generated by Django 2.0 on 2017-12-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loaders', '0007_remove_commissionform_pub_date'),
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
            model_name='commissionform',
            name='form_id',
            field=models.CharField(default='', max_length=6),
        ),
    ]
