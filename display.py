from userclass import User
from credentials import Credentials

 #_________________________________________USERS____________________________________________________________________

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

 #_________________________________________CREDENTIALS____________________________________________________________________

def create_newcredential(account_type, usr_name, password):
    """
    Function for creating new credential for every usr_name
    """
    new_credential = Credentials(account_type, usr_name, password)
    return new_credential

def retain_credential(credentials):
    """
    Save credentials to the credential list
    """
    credentials.save_credential()

def remove_credential(credentials):
    """
    Delete credentials from the credential list
    """
    credentials.delete_credential()    
