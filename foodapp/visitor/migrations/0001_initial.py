# Generated by Django 4.0.4 on 2022-05-13 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown ressource', max_length=30)),
                ('fat', models.FloatField(default=0)),
                ('proteins', models.FloatField(default=0)),
                ('fiber', models.FloatField(default=0)),
                ('carbohydrates', models.FloatField(default=0)),
                ('water', models.FloatField(default=0)),
                ('vitamins', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=3, null=True)),
                ('minerals', models.CharField(choices=[('sodium', 'sodium'), ('calcium', 'calcium'), ('potassium', 'potassium'), ('phosphore', 'phosphore'), ('calcaire', 'calcaire')], max_length=20, null=True)),
                ('kcal', models.FloatField(default=0)),
                ('unit', models.CharField(default=' unit(s) of ', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown ressource', max_length=30)),
                ('fat', models.FloatField(default=0)),
                ('proteins', models.FloatField(default=0)),
                ('fiber', models.FloatField(default=0)),
                ('carbohydrates', models.FloatField(default=0)),
                ('water', models.FloatField(default=0)),
                ('vitamins', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=3, null=True)),
                ('minerals', models.CharField(choices=[('sodium', 'sodium'), ('calcium', 'calcium'), ('potassium', 'potassium'), ('phosphore', 'phosphore'), ('calcaire', 'calcaire')], max_length=20, null=True)),
                ('kcal', models.FloatField(default=0)),
                ('description', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='random menu', max_length=20)),
                ('description', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MenuCommenting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='New comment', max_length=500)),
                ('date', models.DateField(auto_now=True)),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.menu')),
            ],
        ),
        migrations.CreateModel(
            name='MenuAppreciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now=True)),
                ('appreciator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.menu')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='commentors',
            field=models.ManyToManyField(related_name='commentedMenus', through='visitor.MenuCommenting', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='menu',
            name='likers',
            field=models.ManyToManyField(related_name='likedMenus', through='visitor.MenuAppreciation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='menu',
            name='meals',
            field=models.ManyToManyField(related_name='+', to='visitor.meal'),
        ),
        migrations.AddField(
            model_name='menu',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menus', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='MealCommenting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='New comment', max_length=500)),
                ('date', models.DateField(auto_now=True)),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.meal')),
            ],
        ),
        migrations.CreateModel(
            name='MealAppreciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now=True)),
                ('appreciator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.meal')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='commentors',
            field=models.ManyToManyField(related_name='commentedMeals', through='visitor.MealCommenting', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredients',
            field=models.ManyToManyField(blank=True, related_name='+', to='visitor.food'),
        ),
        migrations.AddField(
            model_name='meal',
            name='likers',
            field=models.ManyToManyField(related_name='likedMeals', through='visitor.MealAppreciation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meal',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meals', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meal',
            name='submeals',
            field=models.ManyToManyField(blank=True, to='visitor.meal'),
        ),
    ]
