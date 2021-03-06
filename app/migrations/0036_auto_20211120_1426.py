# Generated by Django 3.2.9 on 2021-11-20 08:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20211120_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='field',
            field=models.CharField(blank=True, choices=[('AppD', 'App Development'), ('SoftD', 'Software Development'), ('WebD', 'Web Development'), ('DgtlM', 'Digtial Marketing')], max_length=50),
        ),
    ]
