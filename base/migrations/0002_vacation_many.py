# Generated by Django 3.0.1 on 2022-05-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacation',
            name='many',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
