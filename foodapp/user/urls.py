from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home_page/', views.home_page, name='home_page'),
    path('log_out/', views.log_out, name='log_out'),
]
