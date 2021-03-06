# Generated by Django 3.2.9 on 2021-11-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20211119_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='quote',
            name='field',
            field=models.CharField(blank=True, choices=[('AppD', 'App Development'), ('SoftD', 'Software Development'), ('WebD', 'Web Development'), ('DgtlM', 'Digtial Marketing')], max_length=50),
        ),
    ]
