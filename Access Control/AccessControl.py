import datetime
from Role import *


class AccessControl():
    def __init__(self):
        
        # Initialize access for Medview Imaging Roles
        self.Patients = Role("Patients")
        self.Administrators = Role("Administrators")
        self.Physicians = Role("Physicians")
        self.Radiologists = Role("Radiologists")
        self.Nurses = Role("Nurses")
        self.Technical_Support = Role("Technical_Support")
        self.setPermissions()

        # Initialize diagnosis for Physicians and Radiologists 
        self.diagnosis = []
        self.treatment = []
        

    # Return system permissions for indicated role.
    def getRole(self, rolename):
        
        if rolename == "Patients":
            return self.Patients
        elif rolename == "Administrators":
            return self.Administrators
        elif rolename == "Physicians":
            return self.Physicians
        elif rolename == "Radiologists":
            return self.Radiologists
        elif rolename == "Nurses":
            return self.Nurses
        elif rolename == "Technical_Support":
            return self.Technical_Support
        else:
            print("The role {} does not exist".format(rolename))
        
    # Method to set the RBAC permissions.
    def setPermissions(self):
        # Set Patient permissions
        patientreadActions = ["patient_profile",'patients_history', "physician_contact", "medical_images"]
        self.Patients.addreadActions(patientreadActions)

        # Set Administrator permissions
        administratorsreadActions = ["patient_profile"]
        self.Administrators.addreadActions(administratorsreadActions)
        administratorswriteActions = ["patient_profile"]
        self.Administrators.addwriteActions(administratorswriteActions)

        # Set Physicians permissions
        physiciansreadActions = ["patient_profile", 'patients_history', "medical_images"]
        self.Physicians.addreadActions(physiciansreadActions)
        physicianswriteActions = ['patients_history']
        self.Physicians.addwriteActions(physicianswriteActions)

        # Set Radiologists permissions
        radiologistsreadActions = ["patient_profile", 'patients_history', "medical_images"]
        self.Radiologists.addreadActions(radiologistsreadActions)
        radiologistswriteActions = ['patients_history']
        self.Radiologists.addwriteActions(radiologistswriteActions)
        
        # Set Nurses permissions
        nursesreadActions = ["patient_profile", 'patients_history', "medical_images"]
        self.Nurses.addreadActions(nursesreadActions)

        # Set Technical permissions
        Techninal_Support_Diagnostics = ["equipment_diagnostics"]
        self.Technical_Support.addDiagnostics(Techninal_Support_Diagnostics)

    # Set attribute-based access controls specific to an authenticated user.
    def setABAC(self, role):
        # Get current time
        current_time = datetime.datetime.now()
        current_hour = current_time.strftime("%H")
        print("Current hour is: " + current_hour + ":00")
        hour = int(current_hour)
        userrole = self.getRole(role)
        
        # Administrator role can only log in to system from 9 - 5.
        if userrole.getRoleEnum(role) == "Administrators":
            if (hour < 9 or hour > 16):
                print (" The system is only available between 9:00 AM and 5:00 PM")
                return False
        return True

    # Implementation of object access control.
    def completeAction(self, role, action, object, write_type):
        userrole = self.getRole(role)
        if action == "read":
            for elems in userrole.getreadActions():
                if object == elems:
                    print("Aceess is granted")
                    return True    
            print("Try Again")
        
        elif action == "write":
            for elems in userrole.getwriteActions():
                if object == elems:
                    print ('Access is granted')
                    
                    # Only Physicians and Radiologist can access patient_history
                    if elems == "patients_history":
                        if userrole.getRoleEnum(role) == "Radiologists" or userrole.getRoleEnum(role) == "Physicians":
                            if write_type == "diagnosis":
                                print("diagnosis made")
                                self.diagnosis.append("diagnosis")
                        if userrole.getRoleEnum(role) == "Physicians":
                            if  write_type == "treatment":
                                print("treatment suggested")
                                self.treatment.append("treatment")                    
                    return True 
            print("Try Again")
        
        elif action == "seek":
            # Only Technical_Support can access this
            if userrole.getRoleEnum(role) == "Technical_Support":
                for elems in userrole.getDiagnostics():
                    if object == elems:
                        print("running diagnostics")
                        return True
                print("Try Again")
        
        #Logout
        elif action == "exit":
            print("Bye!")
            return False
        return True

# t1 = AccessControl()
# print(t1.completeAction("Radiologists", "read", "patients_history", None))
# print(t1.completeAction("Physicians", "write", "patients_history", "treatment"))
# print(t1.completeAction("Technical_Support", "seek", "equipment_diagnostics", None))
# print(t1.diagnosis)
# print(t1.treatment)
