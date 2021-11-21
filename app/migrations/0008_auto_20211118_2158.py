# Generated by Django 3.2.9 on 2021-11-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211118_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careers',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='quote',
            name='field',
            field=models.CharField(choices=[('WebD', 'Web Development'), ('SoftD', 'Software Development'), ('AppD', 'App Development'), ('DgtlM', 'Digtial Marketing')], max_length=50),
        ),
    ]
