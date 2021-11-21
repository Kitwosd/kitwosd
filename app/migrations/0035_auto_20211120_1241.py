# Generated by Django 3.2.9 on 2021-11-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20211120_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='field',
            field=models.CharField(blank=True, choices=[('WebD', 'Web Development'), ('SoftD', 'Software Development'), ('DgtlM', 'Digtial Marketing'), ('AppD', 'App Development')], max_length=50),
        ),
    ]