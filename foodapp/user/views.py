from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.db import transaction
from visitor.models import *
from visitor.views import sorting_functions

import pickle

from visitor.requirement import *

folder = 'user'

@login_required
def home_page(request):
    '''
        Open the current user's home page
    '''
    content = get_random_content()

    return render(request, folder + '/home_page.html', {'content': content})


def log_out(request):
    '''
        log out the current user
    '''
    auth.logout(request)
    return HttpResponseRedirect('/visitor/log_in')


@login_required
@transaction.atomic
def modify_infos(request):
    '''
        Enable the current user (logged in) to modify his/her account informations
    '''
    if request.method=='GET':
        return render(request, 'user/modify_infos.html', {'content':request.user})
    else:
        user = request.user
        user.set_infos(username=request.POST.get('username'), mail=request.POST.get('mail'))
        user.save()

        return HttpResponseRedirect('/user/home_page')



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



@login_required
def my_meals(request):
    '''
        Display Meal objects managed by the current user
    '''
    meals = get_list_or_404(Meal, operator=request.user)

    return render(request, folder + '/meals.html', {'content':meals})




@login_required
def all_menus(request):
    '''
        Display all available Menu objects in the database
    '''
    menus = get_list_or_404(Menu)

    return render(request, folder + '/menus.html', {'content':menus})



@login_required
def my_menus(request):
    '''
        Display Menu objects managed by the current user
    '''
    menus = get_list_or_404(Menu, operator=request.user)

    return render(request, folder + '/menus.html', {'content':menus})


def food_detail(request, id):
    '''
        Display details about a Food object
    '''
    food = get_object_or_404(Food, id=id)
    
    return render(request, folder + '/detail.html', {'content':food})


def meal_detail(request, id):
    '''
        Display details about a Meal object
    '''
    meal = get_object_or_404(Meal, id=id)
    
    return render(request, folder + '/detail.html', {'content':meal})


def menu_detail(request, id):
    '''
        Display details about a Menu object
    '''
    menu = get_object_or_404(Menu, id=id)
    
    return render(request, folder + '/menu_detail.html', {'content':menu})




#################################################################################################################################################################
################################################################## Interact with content ########################################################################
#################################################################################################################################################################

@login_required
@transaction.atomic
def like_content(request, id:int, tp:str):
    '''
        Add a like appreciation to a meal or a menu
    '''

    if tp=='meal':
        # Add a like appreciation to a meal
        meal=Meal.objects.get(id=id)
        try:
            app=MealAppreciation.objects.get(appreciator=request.user, meal=meal)
            app.delete()
        except:
            MealAppreciation.objects.create(appreciator=request.user, meal=meal)
        
        return HttpResponse(str(meal.count_likers()))
    else:
        # Add a like appreciation to a menu
        menu=Menu.objects.get(id=id)
        try:
            app=MealAppreciation.objects.get(appreciator=request.user, meal=menu)
            app.delete()
        except:
            MealAppreciation.objects.create(appreciator=request.user, meal=menu)

        return HttpResponse(str(meal.count_likers()))



@login_required
@transaction.atomic
def comment_content(request, id:int, tp:str, comment:str):
    '''
        Add a comment to a meal or a menu
    '''

    if tp=='meal':        
        # Add a comment on a meal
        meal=Meal.objects.get(id=id)
        MealCommenting.objects.create(commentor=request.user, meal=meal, content=comment)
        
        return HttpResponse(str(meal.count_commentors()))
    else:
        # Add a comment on a menu
        menu=Menu.objects.get(id=id)
        MenuCommenting.objects.create(commentor=request.user, meal=menu, content=comment)

        return HttpResponse(str(menu.count_commentors()))




#################################################################################################################################################################
################################################################## Manage content ########################################################################
#################################################################################################################################################################

@login_required
@transaction.atomic
def modify_content(request, id, tp):

    if tp=='meal':
        return modify_meal(request, id)
    if tp=='menu':
        return modify_menu(request, id)


@login_required
@transaction.atomic
def delete_content(request, id, tp):

    if tp=='meal':
        return delete_meal(request, id)
    if tp=='menu':
        return delete_menu(request, id)




@login_required
@transaction.atomic
def create_meal(request):
    '''
        Manage the creation of a Meal object
    '''

    new_meal = Meal.objects.create(
        name=request.POST.get('name'),
        description=request.POST.get('description'),
        picture=request.FILE.get('picture')
    )

    new_meal.ingredients = request.POST.get('ingredients')
    new_meal.submeals = request.POST.get('submeals')
    new_meal.update_infos()
    new_meal.save()

    return render(request, 'user/home_page', {})


@login_required
@transaction.atomic
def create_menu(request):
    '''
        Manage the creation of a Menu object
    '''

    new_menu = Menu.objects.create(
        name=request.POST.get('name'),
        description=request.POST.get('description'),
    )

    new_menu.meals = request.POST.get('submeals')
    new_menu.save()

    return render(request, 'user/home_page', {})


@login_required
@transaction.atomic
def delete_meal(request, id):
    '''
        Manage the deletion of a Meal object
    '''
    meal = get_object_or_404(Meal, id=id, user=request.user)
    meal.delete()

    return render(request, 'user/home_page', {})


@login_required
@transaction.atomic
def delete_menu(request, id):
    '''
        Manage the deletion of a Menu object
    '''
    menu = get_object_or_404(Menu, id=id, user=request.user)
    menu.delete()

    return render(request, 'user/home_page', {})



@login_required
@transaction.atomic
def modify_meal(request, id):
    '''
        Update a Meal object
    '''

    if request.method=='GET':
        return render(request, 'user/modify_meal.html', {'content': get_object_or_404(Meal, id=id, user=request.user)})
    else:
        meal = get_object_or_404(Meal, id=id, user=request.user)
        meal.name = request.POST.get('name')
        meal.description = request.POST.get('description'),
        
        if request.FILE.get('picture'):
            meal.picture = request.FILE.get('picture')
        if request.POST.get('ingredients'):
            meal.ingredients = request.FILE.get('ingredients')
        if request.FILE.get('submeals'):
            meal.submeals = request.FILE.get('submeals')
        
        meal.save()
        meal.update_infos()
        meal.save()

        return render(request, 'user/home_page', {})



@login_required
@transaction.atomic
def modify_menu(request, id):
    '''
        Update a Menu object
    '''
    if request.method=='GET':
        return render(request, 'user/modify_menu.html', {'content': get_object_or_404(Menu, id=id, user=request.user)})
    else:

        menu = get_object_or_404(Menu, id=id, user=request.user)
        menu.name = request.POST.get('name')
        menu.description = request.POST.get('description'),
        
        if request.FILE.get('meals'):
            menu.meals = request.FILE.get('meals')
        
        menu.save()

        return render(request, 'user/home_page', {})





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
