# Generated by Django 4.0.4 on 2022-05-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0002_food_creation_date_meal_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='picture',
            field=models.ImageField(default='file', upload_to=''),
        ),
        migrations.AddField(
            model_name='meal',
            name='picture',
            field=models.ImageField(default='file', upload_to=''),
        ),
    ]