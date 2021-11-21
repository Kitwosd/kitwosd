# Generated by Django 3.2.9 on 2021-11-18 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_auto_20211118_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='project/'),
        ),
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='team_member/'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='field',
            field=models.CharField(choices=[('SoftD', 'Software Development'), ('DgtlM', 'Digtial Marketing'), ('AppD', 'App Development'), ('WebD', 'Web Development')], max_length=50),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('published_date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('vote', models.IntegerField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]