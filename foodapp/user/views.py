from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.db import transaction
from visitor.models import *
from visitor.views import sorting_functions

import pickle

from visitor.requirement import *
from .forms import *

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
    foods = Food.objects.all()

    return render(request, folder + '/foods.html', {'content':foods})




def all_meals(request):
    '''
        Display all available Meal objects in the database
    '''
    meals = Meal.objects.all()

    return render(request, folder + '/meals.html', {'content':meals})



@login_required
def my_meals(request):
    '''
        Display Meal objects managed by the current user
    '''
    meals = Meal.objects.filter(operator=request.user)

    return render(request, folder + '/meals.html', {'content':meals})




@login_required
def all_menus(request):
    '''
        Display all available Menu objects in the database
    '''
    menus = Menu.objects.all()

    return render(request, folder + '/menus.html', {'content':menus})



@login_required
def my_menus(request):
    '''
        Display Menu objects managed by the current user
    '''
    menus = Menu.objects.filter(operator=request.user)

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
        element = Meal.objects.get(id=id)
        comments = MealCommenting.objects.filter(meal_id=id)
    else:
        element = Menu.objects.get(id=id)
        comments = MenuCommenting.objects.filter(menu_id=id)

    return render(request, folder +'/comments.html', {'element': element, 'comments': comments})



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
            app = get_object_or_404(MealAppreciation, appreciator=request.user, meal=meal)
            app.delete()
        except:
            MealAppreciation.objects.create(appreciator=request.user, meal=meal)

        return HttpResponse(str(meal.count_likers()))
    else:
        # Add a like appreciation to a menu
        menu=Menu.objects.get(id=id)
        try:
            app = get_object_or_404(MenuAppreciation, appreciator=request.user, menu=menu)
            app.delete()
        except:
            MenuAppreciation.objects.create(appreciator=request.user, menu=menu)

        return HttpResponse(str(menu.count_likers()))



@login_required
@transaction.atomic
def comment_content(request, id:int, tp:str, comment:str):
    '''
        Add a comment to a meal or a menu
    '''

    if tp=='meal':        
        # Add a comment on a meal
        meal=get_object_or_404(Meal, id=id)
        MealCommenting.objects.create(commentor=request.user, meal=meal, content=comment)
        
        return HttpResponse(str(meal.count_commentors()))
    else:
        # Add a comment on a menu
        menu=get_object_or_404(Menu, id=id)
        MenuCommenting.objects.create(commentor=request.user, menu=menu, content=comment)

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

    if request.method == 'GET':
        form = MealForm()
        return render(request, 'user/create_meal.html', {'form':form})
    else:
        form = MealForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            picture = request.FILES.get('picture')
            ingredients = form.cleaned_data['ingredients']
            submeals = form.cleaned_data['submeals']
        
            new_meal = Meal.objects.create(
                name=name,
                description=description,
                picture=picture,
                operator=request.user
            )

            new_meal.ingredients.set(ingredients)
            new_meal.submeals.set(submeals)
            new_meal.update_infos()
            new_meal.save()
    
            return HttpResponseRedirect('/user/my_meals/')
        else:
            print(request.POST)
            form = MealForm()
            return render(request, 'user/create_meal.html', {'errors':form.errors.items(), 'form': form})        



@login_required
@transaction.atomic
def create_menu(request):
    '''
        Manage the creation of a Menu object
    '''


    if request.method == 'GET':
        form = MenuForm()
        return render(request, 'user/create_menu.html', {'form':form})
    else:
        form = MenuForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            meals = form.cleaned_data['meals']
        
            new_menu = Menu.objects.create(
                name=name,
                description=description,
                operator=request.user
            )

            new_menu.meals.set(meals)
            new_menu.save()
    
            return HttpResponseRedirect('/user/my_menus/')
        else:
            print(request.POST)
            form = MenuForm()
            return render(request, 'user/create_menu.html', {'errors':form.errors.items(), 'form': form})        



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
        meal.set_name(request.POST.get('name'))
        meal.set_description(request.POST.get('description'))
        
        if request.FILE.get('picture'):
            meal.picture = request.FILE.get('picture')
        if request.POST.get('ingredients'):
            meal.ingredients = request.POST.get('ingredients')
        if request.FILE.get('submeals'):
            meal.submeals = request.POST.get('submeals')
        
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
        menu.set_name(request.POST.get('name'))
        menu.set_description(request.POST.get('description'))
        
        if request.FILE.get('meals'):
            menu.meals = request.POST.get('meals')
        
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
