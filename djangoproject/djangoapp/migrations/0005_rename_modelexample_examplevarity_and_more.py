# Generated by Django 5.0.6 on 2024-06-02 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0004_examplecertificate_examplereview_examplestore'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ModelExample',
            new_name='ExampleVarity',
        ),
        migrations.RenameField(
            model_name='examplecertificate',
            old_name='exampleCertificate',
            new_name='exampleCertificateName',
        ),
        migrations.RenameField(
            model_name='examplestore',
            old_name='name',
            new_name='storeName',
        ),
    ]
