from . import views
from django.urls import path

urlpatterns = [
    # Home
    path('', views.home_page, name='home_page'),
    path('home_page/', views.home_page, name='home_page'),
    
    #Account
    path('log_out/', views.log_out, name='log_out'),
    path('modify_infos/', views.modify_infos, name='modify_infos'),

    # Display content
    path('all_foods/', views.all_foods, name='all_foods'),
    path('all_menus/', views.all_menus, name='all_menus'),
    path('all_meals/', views.all_meals, name='all_meals'),
    path('my_meals/', views.my_meals, name='my_meals'),
    path('my_menus/', views.my_menus, name='my_menus'),
    path('food_detail/<int:id>/', views.food_detail, name='food_detail'),
    path('meal_detail/<int:id>/', views.meal_detail, name='meal_detail'),
    path('menu_detail/<int:id>/', views.menu_detail, name='menu_detail'),


    #Manage content
    path('create_meal/', views.create_meal, name='create_meal'),
    path('create_menu/', views.create_menu, name='create_menu'),
    path('modify_content/<int:id>/<str:tp>/', views.modify_content, name='modify_content'),
    path('delete_content/<int:id>/<str:tp>/', views.delete_content, name='delete_content'),

    #Interact with content
    path('like_content/<int:id>/<str:tp>/', views.like_content, name='like_content'),
    path('comment_content/<int:id>/<str:tp>/<str:comment>/', views.comment_content, name='comment_content'),

    #search
    path('search/<str:filter>/<int:order>', views.search, name='search'),
]
