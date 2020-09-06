import random
import string
import pyperclip

class User():
    """ 
    This is a user class that instantiates new users
    """
    users = []

    def __init__(self, user_name, password):
        """
        A method for defining user properties
        """
        self.user_name = user_name
        self.password = password

    def save_user(self):    
        """
        Method for saving a new user
        """

        User.users.append(self)

    def delete_user(self):
        User.users.remove(self)    

    @classmethod
    def display_user(cls):
        for user in cls.users:
            return user

        # return cls.users    

    