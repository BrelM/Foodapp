from django.urls import re_path, path

from . import views

urlpatterns = [
    path('registration/', views.register, name='registration'),
    path('login/', views.log_in, name='log_in'),

]
