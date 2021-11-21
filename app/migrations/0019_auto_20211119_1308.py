# Generated by Django 3.2.9 on 2021-11-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20211119_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='document',
            field=models.FileField(blank=True, upload_to='quote_file/'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='field',
            field=models.CharField(blank=True, choices=[('WebD', 'Web Development'), ('AppD', 'App Development'), ('DgtlM', 'Digtial Marketing'), ('SoftD', 'Software Development')], max_length=50),
        ),
    ]
