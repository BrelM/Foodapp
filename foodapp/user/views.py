from django.shortcuts import render

from visitor.requirement import *


def home_page(request):
    '''
        Open the current user's home page
    '''
    content = get_random_content(request.user)

    return render('user/home_page.html', {'content': content})


