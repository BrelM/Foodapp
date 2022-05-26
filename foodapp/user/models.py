from django.db import models
from django.contrib.auth.models import AbstractUser



class Operator(AbstractUser):
    '''
    Implementation of a new user class inheriting from django user model class
    This new model will have attribute is_superuser set to True for application administrators accounts and to False for simple operators
    '''
    def get_username(self) -> str:
        return self.username

    def get_mail(self) -> str:
        return self.email

    def setInfos(self, username:str=None, mail:str=None):
        if username:
            self.username = username
        if mail:
            self.email = mail

    def __repr__(self) -> str:
        if self.is_superuser:
            return 'Admin : '+self.username
        else:
            return 'Operator : '+self.username

    def __str__(self) -> str:
        return self.__repr__()