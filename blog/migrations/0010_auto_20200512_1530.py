# Generated by Django 3.0.3 on 2020-05-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200511_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='related_image',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
