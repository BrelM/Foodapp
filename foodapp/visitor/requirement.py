from django.http import HttpResponseRedirect
from .models import Operator
from visitor.models import *

import random


def require_login(request):
    '''
        Check if the current user is anonymous or not.
        If yes, redirect him/her to the login page.
    '''
    if not request.user:
        return HttpResponseRedirect('visitor/log_in')


def get_random_content() -> list:
    '''
        Fetch random content from the database to fill the user's home page
    '''
    elements = list(Food.objects.all()) + list(Meal.objects.all()) + list(Menu.objects.all())
    random.shuffle(elements)

    return elements



def sort_by_type(result:list=[], reverse:int=0) -> dict:
    '''Sort a list of Food, Meal or Menu objects (by types)'''
    if result != []:
        results = {'Food': [], 'Meal' : [], 'Menus' : []}
        for i in range(1, len(result)):
            if isinstance(i, Food):
                results['Food'].append(i)
            if isinstance(i, Meal):
                results['Meal'].append(i)
            if isinstance(i, Menu):
                results['Menu'].append(i)
    return results



def sort_by_name(result:list=[], reverse:int=0) -> list:
    '''Sort a list of Food, Meal or Menu objects (by names) using an insert sort'''
    if result != []:
        for i in range(1, len(result)):
            temp = result[i]
            j = i
            while j > 0 and temp.name.casefold() < result[j-1].name.casefold():
                result[j] = result[j-1]
                j -= 1
            if result[j] != temp:
                result[j] = temp
        if reverse:
            result.reverse()
    return list(result)


def sort_by_date(result:list=[], reverse:int=0) -> list:
    '''Sort a list of Food, Meal or Menu objects (by dates) using an insert sort'''
    if result != []:
        for i in range(1, len(result)):
            temp = result[i]
            j = i
            while j > 0 and temp.creation_date < result[j-1].creation_date:
                result[j] = result[j-1]
                j -= 1
            if result[j] != temp:
                result[j] = temp
        if reverse:
            result.reverse()
    return list(result)

def sort_by_fat(result:list=[], reverse:int=0) -> list:
    '''Sort a list of Food, Meal or Menu objects (by fat) using an insert sort'''
    if result != []:
        for i in range(1, len(result)):
            temp = result[i]
            j = i
            while j > 0 and temp.fat < result[j-1].fat:
                result[j] = result[j-1]
                j -= 1
            if result[j] != temp:
                result[j] = temp
        if reverse:
            result.reverse()
    return list(result)

def sort_by_proteins(result:list=[], reverse:int=0) -> list:
    '''Sort a list of Food, Meal or Menu objects (by proteins) using an insert sort'''
    if result != []:
        for i in range(1, len(result)):
            temp = result[i]
            j = i
            while j > 0 and temp.proteins < result[j-1].proteins:
                result[j] = result[j-1]
                j -= 1
            if result[j] != temp:
                result[j] = temp
        if reverse:
            result.reverse()
    return list(result)

def sort_by_carbohydrates(result:list=[], reverse:int=0) -> list:
    '''Sort a list of Food, Meal or Menu objects (by carbohydrates) using an insert sort'''
    if result != []:
        for i in range(1, len(result)):
            temp = result[i]
            j = i
            while j > 0 and temp.carbohydrates < result[j-1].carbohydrates:
                result[j] = result[j-1]
                j -= 1
            if result[j] != temp:
                result[j] = temp
        if reverse:
            result.reverse()
    return list(result)

def sort_by_fiber(result:list=[], reverse:int=0) -> list:
    '''Sort a list of Food, Meal or Menu objects (by fiber) using an insert sort'''
    if result != []:
        for i in range(1, len(result)):
            temp = result[i]
            j = i
            while j > 0 and temp.fiber < result[j-1].fiber:
                result[j] = result[j-1]
                j -= 1
            if result[j] != temp:
                result[j] = temp
        if reverse:
            result.reverse()
    return list(result)

def sort_by_water(result:list=[], reverse:int=0) -> list:
    '''Sort a list of Food, Meal or Menu objects (by water) using an insert sort'''
    if result != []:
        for i in range(1, len(result)):
            temp = result[i]
            j = i
            while j > 0 and temp.water < result[j-1].water:
                result[j] = result[j-1]
                j -= 1
            if result[j] != temp:
                result[j] = temp
        if reverse:
            result.reverse()
    return list(result)

def sort_by_kcal(result:list=[], reverse:int=0) -> list:
    '''Sort a list of Food, Meal or Menu objects (by kcal) using an insert sort'''
    if result != []:
        for i in range(1, len(result)):
            temp = result[i]
            j = i
            while j > 0 and temp.kcal < result[j-1].kcal:
                result[j] = result[j-1]
                j -= 1
            if result[j] != temp:
                result[j] = temp
        if reverse:
            result.reverse()
    return list(result)
