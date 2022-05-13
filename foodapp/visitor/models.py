from django.db import models
from user.models import Operator



VITAMINS = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D','D'),
        ('E', 'E')
    )
MINERALS = [
    ('sodium', 'sodium'),
    ('calcium', 'calcium'),
    ('potassium', 'potassium'),
    ('phosphore', 'phosphore'),
    ('calcaire', 'calcaire'),
]



class Food(models.Model):
    '''
        Implementation of Food class
    '''
    name = models.CharField(max_length=30, null=False, default='unknown food')
    unit = models.CharField(max_length=50, null=False, default=' unit(s) of ')
    fat = models.FloatField(default=0)
    proteins = models.FloatField(default=0)
    fiber = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)
    water = models.FloatField(default=0)
    vitamins = models.CharField(choices=VITAMINS, max_length=3, null=True)
    minerals = models.CharField(choices=MINERALS, max_length=20, null=True)
    kcal = models.FloatField(default=0)
    #picture = models.ImageField()







class Meal(models.Model):
    '''
        Implementation of Meal class
        A meal might be composed of Food objects but also of Meals objects
    '''
    name = models.CharField(max_length=30, null=False, default='unknown food')
    recipe = models.CharField(max_length=2000, null=False, default='Preparation:\ncooking phase:\n')
    fat = models.FloatField(default=0)
    proteins = models.FloatField(default=0)
    fiber = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)
    water = models.FloatField(default=0)
    vitamins = models.CharField(choices=VITAMINS, max_length=3)
    minerals = models.CharField(choices=MINERALS, max_length=20)
    kcal = models.FloatField(default=0)
    #picture = models.ImageField()

    ingredients = models.ManyToManyField(Food, related_name='+', blank=True)
    submeals = models.ManyToManyField('self', blank=True)
    operator = models.ForeignKey(Operator, related_name='meals', blank=True, null=True, on_delete=models.CASCADE)
    likers = models.ManyToManyField(Operator, related_name='likedMeals', through='MealAppreciation')
    commentors = models.ManyToManyField(Operator, related_name='commentedMeals', through='MealCommenting')








class Menu(models.Model):
    '''
        Implementation of the Menu class
        A menu might contain Meal objects
    '''
    name = models.CharField(max_length=20, null=False, default='random menu')
    description = models.CharField(max_length=50, blank=True)

    meals = models.ManyToManyField(Meal, related_name='menus', blank=False)
    operator = models.ForeignKey(Operator, related_name='menus', blank=True, null=True, on_delete=models.CASCADE)
    likers = models.ManyToManyField(Operator, related_name='likedMenus', through='MenuAppreciation')
    commentors = models.ManyToManyField(Operator, related_name='commentedMenus', through='MenuCommenting')



class MealAppreciation(models.Model):
    '''
        Implementation of the appreciation many to many relationship between Operator model and Meal model
    '''
    appreciator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    value = models.BooleanField(default=True)
    date = models.DateField(auto_now=True)



class MealCommenting(models.Model):
    '''
        Implementation of the commenting many to many relationship between Operator model and Meal model
    '''
    commentor = models.ForeignKey(Operator, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    content = models.BooleanField(default=True)
    date = models.DateField(auto_now=True)





class MenuAppreciation(models.Model):
    '''
        Implementation of the appreciation many to many relationship between Operator model and Menu model
    '''
    appreciator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    meal = models.ForeignKey(Menu, on_delete=models.CASCADE)
    value = models.BooleanField(default=True)
    date = models.DateField(auto_now=True)



class MenuCommenting(models.Model):
    '''
        Implementation of the commenting many to many relationship between Operator model and Menu model
    '''
    commentor = models.ForeignKey(Operator, on_delete=models.CASCADE)
    meal = models.ForeignKey(Menu, on_delete=models.CASCADE)
    content = models.BooleanField(default=True)
    date = models.DateField(auto_now=True)










