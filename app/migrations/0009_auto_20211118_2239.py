# Generated by Django 3.2.9 on 2021-11-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20211118_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='careers',
            old_name='experience',
            new_name='work_experience',
        ),
        migrations.AddField(
            model_name='careers',
            name='education',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='field',
            field=models.CharField(choices=[('AppD', 'App Development'), ('WebD', 'Web Development'), ('DgtlM', 'Digtial Marketing'), ('SoftD', 'Software Development')], max_length=50),
        ),
    ]
