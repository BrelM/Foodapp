from django.forms import ModelForm, TextInput, MultipleChoiceField
from django import forms
from visitor.models import Food, Meal, Menu


class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'description', 'ingredients', 'submeals', 'picture']

        widget = {
            'name': TextInput(attrs={'class': 'input-login'}),
            'description': TextInput(attrs={'class': 'input-login'}),
        }


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'meals']

'''
class MealForm(forms.Form):

    name = forms.CharField(
        label='Name',
        max_length=30,
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Name'}),
        required=True
    )
    description = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Description'})
    )

    ingredients = forms.MultipleChoiceField(
        label='Ingredients',
        choices=list(Food.objects.all()),
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Select the ingredients of your meal'}),
        required=True,
    )

    submeals = forms.ModelMultipleChoiceField(
        label='Submeals',
        queryset=Meal.objects.all(),
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Select the meals composing your meal (optiional)'}),
    )



class MenuForm(forms.Form):

    name = forms.CharField(
        label='Name',
        max_length=30,
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Name'}),
        required=True
    )
    
    description = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Description'}),
        required=True
    )

    meals = forms.ModelMultipleChoiceField(
        label='Submeals',
        queryset=Meal.objects.all(),
        widget=forms.TextInput(attrs={'class':'', 'placeholder':'Select the meals composing your meal (optiional)'}),
    )




'''