from Password import *
from AccessControl import *

class Userlogin():
    def __init__(self):
        print("Welcome to MedView Imaging Systems \n")
        self.passwd = Password()
        self.policy = AccessControl()
        while True:
            self.username = input("Enter Username: \n") #Asks for username
            self.password = input("Enter password: \n") #Asks for password
            self.user = self.passwd.retrieveRecord(self.username, self.password) #Retrives user record
            if self.user is not None:
                if self.policy.setABAC(self.user.getRole().role): #Sets ABAC policy
                    print(" Login Successful \n")
                    print("Welcome "+ self.user.getUsername())
                    print ('You have access to view or write:\n')
                    self.user.getRole().printActions() #Displays all access
                    self.processActions = True
                    self.separatedinput = None
                    while self.processActions:
                        self.action = input("Enter Action or exit\n")
                        self.separatedinput = self.action.split(" ") #Splits input for action, object and optional write type
                        if len(self.separatedinput)>2: # Contains action, object and optional write type
                            self.processActions = self.policy.completeAction(self.user.getRole().role, self.separatedinput[0], self.separatedinput[1],self.separatedinput[2])
                        elif len(self.separatedinput)>1:# Contains action, object
                            self.processActions = self.policy.completeAction(self.user.getRole().role, self.separatedinput[0], self.separatedinput[1],None)
                        else:# Contains action(exit)
                            self.processActions = self.policy.completeAction(self.user.getRole().role, self.separatedinput[0], None, None)
            else:
                print("Could not validate password")
                
        

def main():
    s1 = Userlogin()

if __name__ == "__main__":
    main()