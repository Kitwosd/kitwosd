# Generated by Django 3.2.9 on 2021-11-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_quote_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='quote',
            name='field',
            field=models.CharField(blank=True, choices=[('DgtlM', 'Digtial Marketing'), ('WebD', 'Web Development'), ('AppD', 'App Development'), ('SoftD', 'Software Development')], max_length=50),
        ),
    ]
