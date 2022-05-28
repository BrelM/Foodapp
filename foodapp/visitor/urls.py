from django.urls import re_path, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.register, name='registration'),
    path('log_in/', views.log_in, name='log_in'),
    path('search/<str:filter>/<int:order>', views.search, name='search'),
    

]
