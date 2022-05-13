from django.db import models
from django.contrib.auth.models import AbstractUser



class Operator(AbstractUser):
    '''
    Implementation of a new user class inheriting from django user model class
    This new model will have attribute is_superuser set to True for application administrators accounts and to False for simple operators
    '''
    pass


