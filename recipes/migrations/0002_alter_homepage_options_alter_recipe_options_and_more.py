# Generated by Django 4.1.7 on 2023-03-04 16:54

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'ordering': ('header',)},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='image_url',
        ),
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/recipes/static/', location=None), upload_to='img/'),
        ),
    ]
