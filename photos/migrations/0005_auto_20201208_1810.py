# Generated by Django 3.1.4 on 2020-12-08 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image_url',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='', upload_to='photos'),
            preserve_default=False,
        ),
    ]