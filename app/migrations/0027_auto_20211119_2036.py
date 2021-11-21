# Generated by Django 3.2.9 on 2021-11-19 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20211119_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='quote',
            name='field',
            field=models.CharField(blank=True, choices=[('AppD', 'App Development'), ('SoftD', 'Software Development'), ('DgtlM', 'Digtial Marketing'), ('WebD', 'Web Development')], max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]
