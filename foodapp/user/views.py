from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db import transaction
from visitor.models import *

import pickle, os

from visitor.requirement import *


def home_page(request):
    '''
        Open the current user's home page
    '''
    content = get_random_content(request.user)

    return render(request, 'user/home_page.html', {'content': content})



#################################################################################################################################################################
################################################################### Display content #############################################################################
#################################################################################################################################################################


def all_foods(request):
    '''
        Display all available Food objects in the database
    '''
    foods = get_list_or_404(Food)

    return render(request, 'user/foods.html', {'foods':foods})




def all_meals(request):
    '''
        Display all available Meal objects in the database
    '''
    meals = get_list_or_404(Meal)

    return render(request, 'user/meals.html', {'meals':meals})



def my_meals(request):
    '''
        Display Meal objects managed by the current user
    '''
    meals = get_list_or_404(Meal, operator=request.user)

    return render(request, 'user/meals.html', {'meals':meals})




def all_menus(request):
    '''
        Display all available Menu objects in the database
    '''
    menus = get_list_or_404(Menu)

    return render(request, 'user/menus.html', {'menus':menus})



def my_menus(request):
    '''
        Display Menu objects managed by the current user
    '''
    meals = get_list_or_404(Menu, operator=request.user)

    return render(request, 'user/menus.html', {'menus':menus})


def food_detail(request, id):
    '''
        Display details about a Food object
    '''
    food = get_object_or_404(Food, id=id)
    
    return render(request, 'user/food_detail.html', {'food':food})


def meal_detail(request, id):
    '''
        Display details about a Meal object
    '''
    meal = get_object_or_404(Meal, id=id)
    
    return render(request, 'user/meal_detail.html', {'meal':meal})


def menu_detail(request, id):
    '''
        Display details about a Menu object
    '''
    menu = get_object_or_404(Menu, id=id)
    
    return render(request, 'user/menu_detail.html', {'menu':menu})





#################################################################################################################################################################
################################################################## Interact with content ########################################################################
#################################################################################################################################################################

@transaction.atomic
def like_meal(request, id):
    '''
        Add a like appreciation to a meal
    '''
    
    if request.GET.get('value'):
        MealAppreciation.objects.create(appreciator=request.user, meal=Menu.objects.get(id=id))
    else:
        MealAppreciation.objects.create(appreciator=request.user, meal=Menu.objects.get(id=id), value=False)



@transaction.atomic
def like_menu(request, id):
    '''
        Add a like appreciation to a menu
    '''
    if request.GET.get('value'):
        MenuAppreciation.objects.create(appreciator=request.user, menu=Menu.objects.get(id=id))
    else:
        MenuAppreciation.objects.create(appreciator=request.user, menu=Menu.objects.get(id=id), value=False)



#################################################################################################################################################################
################################################################### Searching ###################################################################################
#################################################################################################################################################################

def search(request, filter, order):
    '''
        Look for ressources (Food, Meal or Menu objects) satisfying the passed string
    '''
    if request.method == 'GET':
        if filter == 'none':
            results = None
        else:
            with open('results', 'rb') as results_file:
                results_raw = pickle.Unpickler(results_file).load()
                results = results_raw['results']
                filter = results_raw['filter']
                order = results_raw['order']

                # Calls for sorting functions in requirement.py

            context = {
                'results': results,
            }
            return render(request, request, 'user/search.html', context)
    else:
        with open('results', 'wb') as results_file:
            pass