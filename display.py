from userclass import User
from credentials import Credentials

def create_useraccount(user_name, password):
    """
    Creates a new user account.
    """
    new_user = User(user_name, password)
    return new_user

def save_user(user):
    user.save_user()    

def display_user():
    return User.display_user()   

def login_user(user_name, password):
    """
    This function checks if a user exists in the list then allows them to login
    """
    log_user = Credentials.authenticate_user(user_name, password)
    return log_user
