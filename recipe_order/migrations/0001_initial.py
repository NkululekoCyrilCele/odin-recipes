# Generated by Django 4.1.7 on 2023-03-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('recipe_type', models.CharField(max_length=50)),
                ('frosting_type', models.CharField(max_length=50)),
                ('delivery_date', models.DateField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]