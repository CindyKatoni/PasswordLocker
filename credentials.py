from userclass import User
import random
import pyperclip
import string


class Credentials():

    credentials_array = []

    def __init__(self, account_type, usr_name, password):
        self.account_type = account_type
        self.usr_name = usr_name
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
        Method for generating a random password

        """
        password_length = 5


        possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890"

        random_character_list = [random.choice(possible_characters) for i in range(password_length)]
        random_password = "".join(random_character_list)
        return random_password
