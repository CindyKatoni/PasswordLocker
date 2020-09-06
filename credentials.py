from user import User
import random
import pyperclip
import string
class Credentials():
    
    credentials_array = []

    def __init__(self, account_type, user_name, password):
        self.account_type = account_type
        self.user_name = user_name
        self.password = password

    def save_credential(self):
        """
        Method for storing a new credential
        """
        Credentials.credentials_array.append(self)    

    def delete_credential(self):
        """
        Method for deleting existing credential
        """
        Credentials.credentials_array.remove(self)

    @classmethod
    def view_credential(cls, account_type):
        """
        This method is for viewing the account credential and password
        """
        for credential in cls.credentials_array:
            if credential.account_type == account_type:
                return credential    

    @classmethod
    def authenticate_user(cls, user_name, password):
        """
        This method checks the if the user's name and password are correct
        """
        verified_user = ""
        for user in User.users:
            if (user.user_name == user_name and user.password == password):
                verified_user = user.user_name
            return verified_user    

    @classmethod
    def random_password(cls):
        """
        This method generates a random password
        """
        length = 12







