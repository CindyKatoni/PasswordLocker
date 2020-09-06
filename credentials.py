class Credentials():
    
    credentials_array = []

    def __init__(self, account_type, user_name, password):
        self.account_type = account_type
        self.user_name = user_name
        self.password = password

    def new_credential(self):
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
    def view_credentials(cls, account_type):
        """
        This method is for viewing the account credential and password
        """
        for credential in cls.credentials_array:
            if credential.account_type == account_type:
                return credential    

