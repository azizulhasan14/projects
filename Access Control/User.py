from AccessControl import *
from Role import *

class User(Role):
    def __init__(self):
        
        # All the user attributes initialized
        self.username = None
        self.name = None
        self.phone_number = None
        self.email = None
        self.grantAccess = None #Discretionary Access Control
        self.role = None
        
        
    def generateUser(self, username, rolename, name, phone_number, email): # User generated
        self.username = username
        self.name = name
        self.phone_number = str(phone_number)
        self.email = email

        # setting user role based on access policy
        self.policy = AccessControl()
        self.role = self.policy.getRole(rolename) # role fetched from AccessControl

        # setting default access
        self.grantAccess = False

    def getName(self):
        return self.name #gets Name of User

    def getRole(self):
        return self.role    #gets role of User

    def getUsername(self):
        return self.username    #gets username of User

    def getAccess(self):
        return self.grantAccess #gets Access of User

