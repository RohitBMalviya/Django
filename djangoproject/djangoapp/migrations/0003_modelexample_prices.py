# Generated by Django 5.0.6 on 2024-06-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_modelexample_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelexample',
            name='prices',
            field=models.IntegerField(default=0),
        ),
    ]
