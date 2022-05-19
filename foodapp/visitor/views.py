import pickle
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from visitor.models import *

from user.models import Operator
from visitor.requirement import *

# Create your views here.
def index(request):
    content = None #get_random_content(request.user)
    return render(request, 'visitor/index.html', {'content': content})




#################################################################################################################################################################
################################################################### Account #####################################################################################
#################################################################################################################################################################

def register(request):
    '''
        Takes user's informations and create a user object (an account)
    '''
    if request.method == 'GET':
        return render(request, 'register.html', {})
    else:
        user = Operator.objects.create_user(
                username=request.POST.get('name'), 
                password=request.POST.get('password'),
                mail=request.POST.get('mail'),
                is_active=True
            )

        return HttpResponseRedirect('visitor:log_in')


def log_in(request):
    '''
        Verify user's informations and if they are correct, he's set as the current user.
        If not, he's told that the inserted informations aren't valid
    '''
    if request.method == 'GET':
        return render(request, 'visitor/log_in.html')
    else:
        try:
            user = auth.authenticate(username=request.POST.get('name'), password=request.POST.get('password'))
            auth.login(user)

            return HttpResponseRedirect('operator:home_page')
        except:
            return HttpResponseRedirect('visitor/log_in.html', {'error': "Ce compte semble ne pas exister."})



#################################################################################################################################################################
################################################################### Display content #############################################################################
#################################################################################################################################################################


def all_foods(request):
    '''
        Display all available Food objects in the database
    '''
    foods = get_list_or_404(Food)

    return render(request, 'visitor/foods.html', {'foods':foods})




def all_meals(request):
    '''
        Display all available Meal objects in the database
    '''
    meals = get_list_or_404(Meal)

    return render(request, 'visitor/meals.html', {'meals':meals})



def my_meals(request):
    '''
        Display Meal objects managed by the current user
    '''
    meals = get_list_or_404(Meal, operator=request.user)

    return render(request, 'visitor/meals.html', {'meals':meals})




def all_menus(request):
    '''
        Display all available Menu objects in the database
    '''
    menus = get_list_or_404(Menu)

    return render(request, 'visitor/menus.html', {'menus':menus})



def my_menus(request):
    '''
        Display Menu objects managed by the current user
    '''
    meals = get_list_or_404(Menu, operator=request.user)

    return render(request, 'visitor/menus.html', {'menus':menus})


def food_detail(request, id):
    '''
        Display details about a Food object
    '''
    food = get_object_or_404(Food, id=id)
    
    return render(request, 'visitor/food_detail.html', {'food':food})


def meal_detail(request, id):
    '''
        Display details about a Meal object
    '''
    meal = get_object_or_404(Meal, id=id)
    
    return render(request, 'visitor/meal_detail.html', {'meal':meal})


def meanu_detail(request, id):
    '''
        Display details about a Menu object
    '''
    menu = get_object_or_404(Menu, id=id)
    
    return render(request, 'visitor/menu_detail.html', {'menu':menu})



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
            return render(request, request, 'visitor/search.html', context)
    else:
        with open('results', 'wb') as results_file:
            pass