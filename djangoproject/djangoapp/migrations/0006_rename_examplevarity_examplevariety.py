# Generated by Django 5.0.6 on 2024-06-02 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0005_rename_modelexample_examplevarity_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExampleVarity',
            new_name='ExampleVariety',
        ),
    ]
