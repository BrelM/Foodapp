from django.urls import re_path, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.register, name='registration'),
    path('log_in/', views.log_in, name='log_in'),



    # Display content
    path('all_foods/', views.all_foods, name='all_foods'),
    path('all_menus/', views.all_menus, name='all_menus'),
    path('all_meals/', views.all_meals, name='all_meals'),
    path('food_detail/<int:id>/', views.food_detail, name='food_detail'),
    path('meal_detail/<int:id>/', views.meal_detail, name='meal_detail'),
    path('menu_detail/<int:id>/', views.menu_detail, name='menu_detail'),
    path('display_comments/<int:id>/<str:tp>/', views.display_comments, name='display_comments'),


    path('search/<str:filter>/<int:order>', views.search, name='search'),
    

]
