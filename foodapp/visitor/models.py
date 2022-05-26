from django.db import models
from user.models import Operator



class Vitamin(models.Model):
    name= models.CharField(max_length=2, null=True)

        
    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "Vitamin : "+self.name

class Mineral(models.Model):
    name= models.CharField(max_length=2, null=True)

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "Mineral : "+self.name


class Ressource(models.Model):
    '''
        Implementation of Ressource class
        Food and Meal classes inherit it.
    '''

    class Meta:
        abstract = True

    name = models.CharField(max_length=30, null=False, default='unknown ressource')
    description = models.CharField(max_length=300, null=False, default='unknown description')
    creation_date = models.DateField(auto_now=True)
    fat = models.FloatField(default=0)
    proteins = models.FloatField(default=0)
    fiber = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)
    water = models.FloatField(default=0)
    kcal = models.FloatField(default=0)
    picture = models.ImageField(null=True)
    
    vitamins = models.ManyToManyField(Vitamin, related_name='+', blank=True)
    minerals = models.ManyToManyField(Mineral, related_name='+', blank=True)

    # Getters
    def get_name(self) -> str:
        return self.name
    
    def get_description(self) -> str:
        return self.description
    
    def get_creation_date(self) -> models.DateField:
        return self.creation_date

    def get_fat(self) -> float:
        return self.fat

    def get_proteins(self) -> float:
        return self.proteins

    def get_fiber(self) -> float:
        return self.fiber

    def get_carbohydrates(self) -> float:
        return self.carbohydrates

    def get_water(self) -> float:
        return self.water

    def get_vitamins(self) -> list:
        return list(self.vitamins)

    def get_minerals(self) -> list:
        return list(self.minerals)

    def get_kcal(self) -> float:
        return self.kcal

    # Setters
    def set_attributes(self, **kwargs):
        if kwargs['name']:
            self.name = kwargs['name']
        if kwargs['creation_date']:
            self.creation_date = kwargs['creation_date']
        if kwargs['description']:
            self.description = kwargs['description']
        if kwargs['fat']:
            self.fat = kwargs['fat']
        if kwargs['proteins']:
            self.proteins = kwargs['proteins']
        if kwargs['carbohydrates']:
            self.carbohydrates = kwargs['carbohydrates']
        if kwargs['kcal']:
            self.kcal = kwargs['kcal']
        if kwargs['fiber']:
            self.fiber = kwargs['fiber']
        if kwargs['water']:
            self.water = kwargs['water']
        if kwargs['vitamins']:
            self.vitamins = kwargs['vitamins']
        if kwargs['minerals']:
            self.minerals = kwargs['minerals']
    
    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "Food : "+self.name

class Food(Ressource):
    '''
        Implementation of Food class
    '''
    unit = models.CharField(max_length=50, null=False, default=' unit(s) of ')

    def get_unit(self) -> str:
        return self.unit



class Meal(Ressource):
    '''
        Implementation of Meal class
        A meal might be composed of Food objects but also of Meals objects
    '''    
    description = models.CharField(max_length=100, null = True)

    ingredients = models.ManyToManyField(Food, related_name='+', blank=True)
    submeals = models.ManyToManyField('self', blank=True)
    operator = models.ForeignKey(Operator, related_name='meals', blank=True, null=True, on_delete=models.CASCADE)
    likers = models.ManyToManyField(Operator, related_name='likedMeals', through='MealAppreciation')
    commentors = models.ManyToManyField(Operator, related_name='commentedMeals', through='MealCommenting')

    def update_infos(self):
        '''
            Update nutrient attributes values taking in charge the nutrient attributes values of the composing Food objects
        '''

        elements = list(self.elements.all()) + list(self.submeals.all())

        for element in elements:
            self.fat += element.get_fat()
            self.proteins += element.get_proteins()
            self.fiber += element.get_fiber()
            self.carbohydrates += element.get_carbohydrates()
            self.water += element.get_water()
            self.kcal += element.get_kcal()
            self.vitamins += element.get_vitamins()
            self.minerals += element.get_minerals()
    
    def set_name(self, name:str):
        self.name = name




class Menu(models.Model):
    '''
        Implementation of the Menu class
        A menu might contain Meal objects
    '''
    name = models.CharField(max_length=20, null=False, default='random menu')
    creation_date = models.DateField(auto_now=True)
    description = models.CharField(max_length=50, blank=True)

    meals = models.ManyToManyField(Meal, related_name='+', blank=False)
    operator = models.ForeignKey(Operator, related_name='menus', blank=True, null=True, on_delete=models.CASCADE)
    likers = models.ManyToManyField(Operator, related_name='likedMenus', through='MenuAppreciation')
    commentors = models.ManyToManyField(Operator, related_name='commentedMenus', through='MenuCommenting')

    # Getters
    def get_name(self) -> str:
        return self.name
    
    def get_description(self) -> str:
        return self.description
    
    def get_creation_date(self) -> models.DateField:
        return self.creation_date

        # Setters
    def set_name(self, name):
        self.name = name
    
    def set_description(self, description):
        self.description = description

    def set_creation_date(self, date):
        self.creation_date = date

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "Food : "+self.name




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
   
    content = models.CharField(max_length=500, null=False, default='New comment')
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
   
    content = models.CharField(max_length=500, null=False, default='New comment')
    date = models.DateField(auto_now=True)









