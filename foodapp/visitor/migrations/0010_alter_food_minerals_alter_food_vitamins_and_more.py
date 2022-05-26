# Generated by Django 4.0.4 on 2022-05-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0009_alter_food_minerals_alter_food_vitamins_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='minerals',
            field=models.ManyToManyField(blank=True, related_name='+', to='visitor.mineral'),
        ),
        migrations.AlterField(
            model_name='food',
            name='vitamins',
            field=models.ManyToManyField(blank=True, related_name='+', to='visitor.vitamin'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='minerals',
            field=models.ManyToManyField(blank=True, related_name='+', to='visitor.mineral'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='vitamins',
            field=models.ManyToManyField(blank=True, related_name='+', to='visitor.vitamin'),
        ),
    ]