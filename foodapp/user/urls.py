from . import views
from django.urls import path

urlpatterns = [
    path('home_page/', views.home_page, name='home_page'),
    
]
