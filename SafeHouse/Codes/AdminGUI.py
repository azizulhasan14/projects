from tkinter import *
from TSHistory import thingspeak_read_h
from UsersDatabase import *


def addNewUser():
    specs = ""
    if newcamera1:
        specs += "Camera, "
    if newmotion1:
        specs += "MotionSensor, "
    if newbuzzer1:
        specs += "Buzzer, "
    if newfire1:
        specs += "FireSensor, "
    if newlock1:
        specs += "DoorLock, " 
    specs[:-1]
    specs+= "."
    write_database(user_id1.get(), name1.get(), address1.get(), number1.get(), read1.get(), write1.get(), specs)
    return 1
    
def updateExisitingUser():
    specs2 = ""
    if newcamera2:
        specs2 += "Camera, "
    if newmotion2:
        specs2 += "MotionSensor, "
    if newbuzzer2:
        specs2 += "Buzzer, "
    if newfire2:
        specs2 += "FireSensor, "
    if newlock2:
        specs2 += "DoorLock, " 
    specs2[:-1]
    specs2+= "."
    write_database(user_id2.get(), name2.get(), address2.get(), number2.get(), read2.get(), write2.get(), specs2)
    return 1

def readHistory_admin():
    log.set("")
    key = read_database(id_num.get())
    arr = thingspeak_read_h(key,id_num.get(), select.get())
    history= ""
    for x in arr:
        for i in range(5):
            temp=""
            temp+="ID: "
            temp+=(str(x[0]))
            temp+=", Date: "
            temp+=(str(x[1]))
            temp+=", Time: "
            temp+=(str(x[2]))
            temp+=", Sensor: "
            temp+=(str(x[3]))
            temp+=", Video_location: "
            temp+=(str(x[4]))              
        history+= temp +'\n\n'
    log.set(history)
    return 1

# Add new user window
def openNewUser():  
    # Toplevel object which will  
    # be treated as a new window 
    newUser = Toplevel(window)
    # sets the title of the 
    # Toplevel widget 
    newUser.title("Add User") 
    # sets the geometry of toplevel 
    newUser.minsize(1100,220)
    newUser.maxsize(1100,220)
    # A Label widget to show in toplevel 
    Label(newUser,  
          text ="Add a New User", font="none 16 bold").pack() 
    
    Label(newUser, text="Id", fg= "black", font= "none 12").place(x=20, y=45)
    iD = Entry(newUser, textvariable= user_id1, width=5)
    iD.pack()
    iD.place(x=40,y=50)
    
    Label(newUser, text="Name", fg= "black", font= "none 12").place(x=90, y=45)
    name = Entry(newUser, textvariable= name1, width=20)
    name.pack()
    name.place(x=140,y=50)
    
    Label(newUser, text="Address", fg= "black", font= "none 12").place(x=280, y=45)
    address = Entry(newUser, textvariable= address1, width=30)
    address.pack()
    address.place(x=350,y=50) 
    
    Label(newUser, text="Number", fg= "black", font= "none 12").place(x=550, y=45)
    num = Entry(newUser, textvariable= number1, width=15)
    num.pack()
    num.place(x=615,y=50)
    
    Label(newUser, text="Read", fg= "black", font= "none 12").place(x=720, y=45)
    num = Entry(newUser, textvariable= read1, width=20)
    num.pack()
    num.place(x=770,y=50)
    
    Label(newUser, text="Write", fg= "black", font= "none 12").place(x=900, y=45)
    num = Entry(newUser, textvariable= write1, width=20)
    num.pack()
    num.place(x=950,y=50)
     
    Label(newUser, text="Specs:", fg= "black", font= "none 14 bold").place(x=525, y=90)
    
    Checkbutton(newUser, text= "Camera", variable= newcamera1, fg= "black", font= "none 14", width=10, height=2).place(x=290, y=115)
    Checkbutton(newUser, text= "Motion", variable= newmotion1, fg= "black", font= "none 14", width=10, height=2).place(x=400, y=115)
    Checkbutton(newUser, text= "Buzzer", variable= newbuzzer1, fg= "black", font= "none 14", width=10, height=2).place(x=510, y=115)
    Checkbutton(newUser, text= "Fire", variable= newfire1, fg= "black", font= "none 14", width=10, height=2).place(x=620, y=115)
    Checkbutton(newUser, text= "Lock", variable= newlock1, fg= "black", font= "none 14", width=10, height=2).place(x=730, y=115)
    
    submit = Button(newUser, text="Submit", fg= "black", font= "none 12 bold", width=10, height=1, command= addNewUser).place(x=500, y=170)
      

# Edit user window
def openEditUser():  
    # Toplevel object which will  
    # be treated as a new window 
    editUser = Toplevel(window)
    # sets the title of the 
    # Toplevel widget 
    editUser.title("Edit User") 
    # sets the geometry of toplevel 
    editUser.minsize(1100,220)
    editUser.maxsize(1100,220)
    # A Label widget to show in toplevel 
    Label(editUser,  
          text ="Edit an Existing User With Unique ID", font="none 16 bold").pack()
    
    Label(editUser, text="Id", fg= "black", font= "none 12").place(x=20, y=45)
    iD = Entry(editUser, textvariable= user_id2, width=5)
    iD.pack()
    iD.place(x=40,y=50)
    
    Label(editUser, text="Name", fg= "black", font= "none 12").place(x=90, y=45)
    name = Entry(editUser, textvariable= name2, width=20)
    name.pack()
    name.place(x=140,y=50)
    
    Label(editUser, text="Address", fg= "black", font= "none 12").place(x=280, y=45)
    address = Entry(editUser, textvariable= address2, width=30)
    address.pack()
    address.place(x=350,y=50) 
    
    Label(editUser, text="Number", fg= "black", font= "none 12").place(x=550, y=45)
    num = Entry(editUser, textvariable= number2, width=15)
    num.pack()
    num.place(x=615,y=50)
    
    Label(editUser, text="Read", fg= "black", font= "none 12").place(x=720, y=45)
    num = Entry(editUser, textvariable= read2, width=20)
    num.pack()
    num.place(x=770,y=50)
    
    Label(editUser, text="Write", fg= "black", font= "none 12").place(x=900, y=45)
    num = Entry(editUser, textvariable= write2, width=20)
    num.pack()
    num.place(x=950,y=50)
     
    Label(editUser, text="Specs:", fg= "black", font= "none 14 bold").place(x=525, y=90)
        
    Checkbutton(editUser, text= "Camera", variable= newcamera2, fg= "black", font= "none 14", width=10, height=2).place(x=290, y=115)
    Checkbutton(editUser, text= "Motion", variable= newmotion2, fg= "black", font= "none 14", width=10, height=2).place(x=400, y=115)
    Checkbutton(editUser, text= "Buzzer", variable= newbuzzer2, fg= "black", font= "none 14", width=10, height=2).place(x=510, y=115)
    Checkbutton(editUser, text= "Fire", variable= newfire2, fg= "black", font= "none 14", width=10, height=2).place(x=620, y=115)
    Checkbutton(editUser, text= "Lock", variable= newlock2, fg= "black", font= "none 14", width=10, height=2).place(x=730, y=115)
    
    submit = Button(editUser, text="Submit", fg= "black", font= "none 12 bold", width=10, height=1, command= updateExisitingUser).place(x=500, y=170)    



# Request History Window
def openHistory():  
    # Toplevel object which will  
    # be treated as a new window 
    history = Toplevel(window)
    # sets the title of the 
    # Toplevel widget 
    history.title("User History") 
    # sets the geometry of toplevel 
    history.minsize(700,220)
    # A Label widget to show in toplevel 
    Label(history,  
          text ="Pull History of User With Unique ID", font="none 16 bold").pack()
    
    Label(history, text="Insert Desired Id", fg= "black", font= "none 12 bold").place(x=100, y=45)
    iD = Entry(history, textvariable= id_num, width=10)
    iD.pack()
    iD.place(x=230,y=47)
    Label(history, text="Number of History Logs", fg= "black", font= "none 12 bold").place(x=310, y=45)
    OptionMenu(history, select, "1","5", "10","15","20").place(x=500, y=45)
    
    #History Labels     
    Label(history, textvariable=log, justify= LEFT, padx= 2, pady= 2, bg="grey").place(x=120, y=90)
    
    req = Button(history, text="Request", fg= "black", font= "none 12 bold", width=10, height=1, command= readHistory_admin).place(x=570, y=43)
    
        
    

# Create main window
window = Tk()
window.minsize(300,300)
window.maxsize(300,300)
window.title("SafeHouse Admin")
window.configure( background="Black")

#Title
Label(window, text="ADMIN GUI", bg= "black", fg= "lime", font= "none 20 bold").place(x=75, y=20)

##ADD USER BUTTON
#Initilaizing all entry buttons and check boxes
user_id1= StringVar()
name1= StringVar()
address1= StringVar()
number1= StringVar()
read1= StringVar()
write1= StringVar()
newcamera1 = IntVar()
newmotion1 = IntVar()
newbuzzer1 = IntVar()
newfire1 = IntVar()
newlock1 = IntVar()
submit = Button(window, text="Add New User", bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= openNewUser).place(x=50, y=80)

##Edit USER BUTTON
#Initilaizing all entry buttons and check boxes
user_id2= StringVar()
name2= StringVar()
address2= StringVar()
number2= StringVar()
read2= StringVar()
write2= StringVar()
newcamera2 = IntVar()
newmotion2 = IntVar()
newbuzzer2 = IntVar()
newfire2 = IntVar()
newlock2 = IntVar()
submit = Button(window, text=" Edit User ", bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= openEditUser).place(x=50, y=140)

##Get USER History BUTTON
#Initilaizing all entry buttons and check boxes
select = StringVar()
log= StringVar()
id_num = StringVar()
submit = Button(window, text="Request History", bg="lime", fg= "black", font= "none 12 bold", width=20, height=2, command= openHistory).place(x=50, y=200)



x = int(input("To start system press 1/ Press 0 to quit: "))
if x==1:
    window.mainloop()
else:
    print("bye")
