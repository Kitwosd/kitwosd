# Generated by Django 3.2.9 on 2021-11-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20211118_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='field',
            field=models.CharField(choices=[('AppD', 'App Development'), ('SoftD', 'Software Development'), ('DgtlM', 'Digtial Marketing'), ('WebD', 'Web Development')], max_length=50),
        ),
    ]
