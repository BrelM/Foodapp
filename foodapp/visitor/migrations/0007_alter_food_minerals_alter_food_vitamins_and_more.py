# Generated by Django 4.0.4 on 2022-05-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0006_minerals_vitamins_remove_food_minerals_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='minerals',
            field=models.ManyToManyField(related_name='+', to='visitor.minerals'),
        ),
        migrations.AlterField(
            model_name='food',
            name='vitamins',
            field=models.ManyToManyField(related_name='+', to='visitor.vitamins'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='minerals',
            field=models.ManyToManyField(related_name='+', to='visitor.minerals'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='vitamins',
            field=models.ManyToManyField(related_name='+', to='visitor.vitamins'),
        ),
    ]
