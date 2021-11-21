# Generated by Django 3.2.9 on 2021-11-18 13:33

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211117_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='field',
            field=models.CharField(choices=[('AppD', 'App Development'), ('SoftD', 'Software Development'), ('WebD', 'Web Development'), ('DgtlM', 'Digtial Marketing')], max_length=50),
        ),
    ]