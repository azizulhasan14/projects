from RoleEnum import *

class Role(RoleEnum):
    
    def __init__(self, rolename):
        #initiales different actions of the role
       super().__init__(rolename)
       self.readActions = []
       self.writeActions = []
       self.Diagnostics = []

    def getRoleEnum(self, rolename):
        t1 = RoleEnum(rolename)     #gets Role Value
        return t1.getEnum(rolename)

    def addreadActions(self, readAction): #adds read actions
        if type(readAction) is str:
           self.readActions.append(readAction)        
        else:
            self.readActions.extend(readAction)

    def removereadActions(self, readAction):    #removes read actions
        try:
            if self.readActions is not None:
                if type(readAction) is str:
                    self.readActions.remove(readAction)
                else:
                    for elem in readAction:
                        self.readActions.remove(elem)
        except:
            print("Nothing to remove. The list is empty")
    
    def addwriteActions(self, writeAction):      #adds read actions 
        if type(writeAction) is str:
           self.writeActions.append(writeAction)        
        else:
            self.writeActions.extend(writeAction)
    
    def removewriteActions(self, writeAction):  #removes read actions
        try:
            if self.writeActions is not None:
                if type(writeAction) is str:
                    self.writeActions.remove(writeAction)
                else:
                    for elem in writeAction:
                        self.writeActions.remove(elem)
        except:
            print("Nothing to remove. The list is empty")

    def addDiagnostics(self, diagnostics):      #adds diagnostic actions 
        if type(diagnostics) is str:
           self.Diagnostics.append(diagnostics)        
        else:
            self.Diagnostics.extend(diagnostics)
    
    def removeDiagnostics(self, diagnostics):   #removes diagnostic actions
        try:
            if self.Diagnostics is not None:
                if type(diagnostics) is str:
                    self.Diagnostics.remove(diagnostics)
                else:
                    for elem in diagnostics:
                        self.Diagnostics.remove(elem)
        except:
            print("Nothing to remove. The list is empty")
    
    def getreadActions(self):   #get read actions
        return self.readActions
    
    def getwriteActions(self): #get write actions
        return self.writeActions

    def getDiagnostics(self):   #get diagnostic actions
        return self.Diagnostics
    
    def printActions(self): #prints all available actions
        if len(self.readActions)>0:
            for elems in self.readActions:
                print ("read access: "+elems)
        if len(self.writeActions)>0:
            for items in self.writeActions:
                print("write access: " + items)
        if len(self.Diagnostics)>0:
            for items in self.Diagnostics:
                print("Diagnostics access: " + items)