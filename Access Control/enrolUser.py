from Password import *

class enrolUser():
    def __init__(self):
        self.response = "y"
        self.passwd = Password()
        
        while self.response == "y":
            print(" Welcome to MedView Imaging System")
            self.username = input("Enter Username: \n") #Asks for username
            self.username.strip()
            self.trypassword = input("Enter Password: \n")  #Asks for password
            self.trypassword.strip()
            self.password = None
            if self.passwd.passwordChecker(self.username,self.trypassword): #checks password using Password checker
                self.password = self.trypassword
            self.name = input("Enter your name: \n")    #Asks for name
            self.name.strip()
            self.phone = input("Enter your phone number: \n") #Asks for phone number
            self.phone.strip()
            self.email = input("Enter your email address: \n") #Asks for email
            self.email.strip()
            print("The role options are: \n")
            print("Patients, Administrators, Physicians, Radiologists, Nurses, Technical Support")
            self.tryrole = input("Enter your role: \n") #Asks for role
            self.role = None
            if self.passwd.checkuserRole(self.tryrole): #Checks for role using checkuserRole
                self.role = self.tryrole
            if self.passwd.addRecord(self.username, self.password, self.role, self.name, self.phone, self.email): #adds user record
                print("User enrolled")
            else: 
                print("User could not be added")
                break
            self.tryresponse = input("Enroll another user? (y/n)") #Asks to enroll another user
            if self.tryresponse == self.response:
                continue
            else:
                break


def main():
    s1 = enrolUser()

if __name__ == "__main__":
    main()