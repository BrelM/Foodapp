
from django import forms
from .models import Food, Meal


class MealForm(forms.Form):

    name = forms.CharField(
        label='Name',
        max_length=30,
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Enter the name of your meal'}),
        required=True
    )
    description = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Enter the description of your meal'})
    )

    ingredients = forms.ModelMultipleChoiceField(
        label='Ingredients',
        choices=Food.objects.all(),
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Select the ingredients of your meal'}),
        required=True,
    )

    submeals = forms.MultipleChoiceField(
        label='Submeals',
        choices=Meal.objects.all(),
        max_length=30,
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Select the meals composing your meal (optiional)'}),
    )



class MenuForm(forms.Form):

    name = forms.CharField(
        label='Name',
        max_length=30,
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Enter the name of your menu'}),
        required=True
    )
    
    description = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Enter the description of your meal'}),
        required=True
    )

    meals = forms.MultipleChoiceField(
        label='Submeals',
        choices=Meal.objects.all(),
        max_length=30,
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Select the meals composing your meal (optiional)'}),
    )
