from enum import Enum

class RoleEnum:
    
    def __init__(self, role):
        #initializes role
        self.role = role

    class Roles(Enum):      #enum class for all the Medview roles
        Patients = "Patients"
        Administrators = "Administrators"
        Physicians = "Physicians"
        Radiologists = "Radiologists"
        Nurses = "Nurses"
        Technical_Support = "Technical_Support"
    
    def getEnum (self, role):       #gets values from the enum class for the respective role
        
        if role == "Patients":
            return self.Roles.Patients.value
        elif role == "Administrators":
            return self.Roles.Administrators.value
        elif role == "Physicians":
            return self.Roles.Physicians.value
        elif role == "Radiologists":
            return self.Roles.Radiologists.value
        elif role == "Nurses":
            return self.Roles.Nurses.value
        elif role == "Technical_Support":
            return self.Roles.Technical_Support.value
        else:
            print("The role {} does not exist".format(self.role))
