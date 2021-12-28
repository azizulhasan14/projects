import hashlib
import os
from User import *
import base64 

class Password():
    def __init__(self):
        # pasword initializer
        self.weakpasswords = ["Password1", "Qwerty123", "Qaz123wsx"]
        self.filename = "passwd"
        self.salt = os.urandom(16)
    
    # creates pasword file
    def createPasswordFile(self):
        return open("{}.txt".format(self.filename), "a")
    
    def addRecord(self, username, password, role, name, phone, email):
        salted_string = self.createSaltedString(self.salt) 
        saltedhash = self.createSaltedHash(password, self.salt)
        record = ""
        record += username +" : "+ salted_string + " : " + saltedhash +" : " + role #all the attributes are stroed as a record
        record += " : " + name + "," + phone + "," + email
        f = self.createPasswordFile()
        f.write(record+"\n")
        f.close()
        return True
    
    def retrieveRecord(self, username, password):
        attributes = []
        f = open("{}.txt".format(self.filename), "r")
        for line in f:
            attributes = line.split(" : ")
            if attributes[0] == username:
                print("verifying password")
                salt = (self.decodeSaltedString(attributes[1])) #decodes saltedString to verify user
                saltedhash = self.createSaltedHash(password, salt)  

                if saltedhash == attributes[2]: #verfies the salt
                    contact = attributes[4].split(",")
                    new_user = User()
                    new_user.generateUser(attributes[0], attributes[3], contact[0], contact[1], contact[2])
                    f.close()
                    return new_user
        f.close()
        return None

    def createSaltedHash(self, password, salt):
        b_password = str.encode(password)
        dk = hashlib.pbkdf2_hmac('sha256', b_password, salt, 100000)        #creates salted hash using the hmac function
        return dk.hex() 
    
    def createSaltedString(self, salt):       
        base64_bytes = base64.b64encode(salt)       #creates salted string using the b64 encoder
        base64_string = base64_bytes.decode()
        return base64_string
    
    def decodeSaltedString(self, string):
        return  base64.b64decode(string)        #decodes salted string using the b64 decoder

    def passwordChecker(self, username, password):
        if (len(password) < 8 or len(password) > 12): #pasword length should be between 8-12
            print("Password should be 8-12 characters")
            return False
        
        if password == username:    #password cannot be same as username
            print("Password cannot same as the username")
        
        special_Charac = ['!', '@', "#", "$", "%", '?', '*']
        uppercase = False
        lowercase = False
        digit = False
        special_char = False

        for letter in password:
            if letter.isupper(): #password should contain uppercase
                uppercase = True
            
            if letter.islower(): #password should contain lowercase
                lowercase = True

            if letter.isdigit():    #password should contain digit
                digit = True
            
            for characters in special_Charac:   #password should contain special character
                if characters == letter:
                    special_char = True
            
            if letter == password[len(password)-1]: #password should meet all criteria
                if (not uppercase or not lowercase or not digit or not special_char):
                    print("Password must contain an uppercase character, lowercase character, " +
						"number, and a special character from the set {!, @, #, $, %, ?, *}.")
                    return False
        
        for weakpass in self.weakpasswords: #password should not be a weak password
            if password == weakpass:
                print('The entered password is weak')
                return False
        
        return True
    
    def addtoweakpasswords( self, password): #allows dynamic allocation of weak passwords
        self.weakpasswords.append(password)
    
    def checkuserRole(self, role): #checks user role
        user = AccessControl()
        if user.getRole(role):
            return True
        return False

# t1 = Password()
# print(t1.passwordChecker("abc", "Mbkhd4415@"))
# print(t1.passwordChecker("abc", "MBKHD4415@"))
# print(t1.passwordChecker("abc", "mbkhd4415@"))
# print(t1.passwordChecker("abc", "Mbkhdmbkh@"))
# print(t1.passwordChecker("abc", "Mbkhd44151"))
# print(t1.passwordChecker("abc", "Password1!"))

