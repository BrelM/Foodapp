import pickle
from django.db import transaction
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from visitor.models import *

from user.models import Operator
from visitor import requirement

folder = 'visitor'

sorting_functions = {
    'type': requirement.sort_by_type,
    'name': requirement.sort_by_name,
    'fat': requirement.sort_by_fat,
    'proteins': requirement.sort_by_proteins,
    'date': requirement.sort_by_date,
    'carbohydrates': requirement.sort_by_carbohydrates,
    'fiber': requirement.sort_by_fiber,
    'water': requirement.sort_by_water,
    'kcal': requirement.sort_by_kcal
}


# Create your views here.
def index(request):
    content = requirement.get_random_content()
    return render(request, folder + '/index.html', {'content': content})

#################################################################################################################################################################
################################################################### Account #####################################################################################
#################################################################################################################################################################
@transaction.atomic
def register(request):
    '''
        Takes user's informations and create a user object (an account)
    '''
    if request.method == 'GET':
        return render(request, folder + '/registration.html', {})
    else:
        user = Operator.objects.create_user(
                username=request.POST.get('username'), 
                password=request.POST.get('password'),
                email=request.POST.get('mail'),
                is_active=True
            )

        return HttpResponseRedirect('/visitor/log_in/')



def log_in(request):
    '''
        Verify user's informations and if they are correct, he's set as the current user (he's no longer anonymous).
        If not, he's told that the inserted informations aren't valid
    '''
    if request.method == 'GET':
        return render(request, folder + '/log_in.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            
            if user: 
                if user.is_superuser:
                    return HttpResponseRedirect('/admin/')
                else:
                    return HttpResponseRedirect('/user/home_page/')
            else: raise ValueError()
        except:
            return render(request, folder + '/log_in.html', {'error': "Ce compte semble ne pas exister."})



#################################################################################################################################################################
################################################################### Display content #############################################################################
#################################################################################################################################################################


def all_foods(request):
    '''
        Display all available Food objects in the database
    '''
    foods = get_list_or_404(Food)

    return render(request, folder + '/foods.html', {'content':foods})




def all_meals(request):
    '''
        Display all available Meal objects in the database
    '''
    meals = get_list_or_404(Meal)

    return render(request, folder + '/meals.html', {'content':meals})


def all_menus(request):
    '''
        Display all available Menu objects in the database
    '''
    menus = get_list_or_404(Menu)

    return render(request, folder + '/menus.html', {'content':menus})


def food_detail(request, id):
    '''
        Display details about a Food object
    '''
    food = get_object_or_404(Food, id=id)
    
    return render(request, folder + '/detail.html', {'element':food})


def meal_detail(request, id):
    '''
        Display details about a Meal object
    '''
    meal = get_object_or_404(Meal, id=id)
    
    return render(request, folder + '/detail.html', {'element':meal})


def menu_detail(request, id):
    '''
        Display details about a Menu object
    '''
    menu = get_object_or_404(Menu, id=id)
    
    return render(request, folder + '/detail.html', {'element':menu})



def display_comments(request, id, tp):
    '''
        Display all the comments made about a Meal or Menu object
    '''
    if tp=='meal':
        element = get_object_or_404(Meal, id=id)
        comments = get_list_or_404(MealCommenting, meal_id=id)
    else:
        element = get_object_or_404(Menu, id=id)
        comments = get_list_or_404(MenuCommenting, menu_id=id)

    return render(request, folder +'/comments.html', {'element': element, 'comments': comments})



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
                keyword = pickle.Unpickler(results_file).load()
                # Calls for sorting functions in requirement.py
                results = sorting_functions[filter](results_raw, order)

        context = {
            'content': results,
            'keyword': keyword,
        }
        return render(request, folder + '/search.html', context)
    else:
        key = request.POST.get('keyword')
        results = list(Food.objects.filter(name__icontains=key)) + list(Meal.objects.filter(name__icontains=key)) + list(Menu.objects.filter(name__icontains=key))
        
        with open('results', 'wb') as results_file:
            pickle.Pickler(results_file).dump(results)
            pickle.Pickler(results_file).dump(key)
            
        return render(request, folder + '/search.html', {'content' : results, 'keyword': key})
