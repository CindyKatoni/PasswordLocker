class Credentials(self, account_type, user_name, password):
    
    credentials = []

    def __init__(self, account_type, user_name, password):
        self.account_type = account_type
        self.user_name = user_name
        self.password = password

    def new_credential(self):
        """
        Method for storing a new credential
        """
        Credentials.credentials.append(self)    

    def delete_credential(self):
        """
        Method for deleting existing credential
        """
        Credentials.credentials.remove(self)
