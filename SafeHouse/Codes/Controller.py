from TSHistory import thingspeak_write_h
from TSCommand import thingspeak_read_c
# from Camera import*
from Buzzer import*
from Lock import*
from Motion import*
from Flame import*
import datetime
import time
import picamera

##ThingSpeak Channels' Information 
ID = "1160874" # TS Command ID
READ_KEY="YOLQ8V4RT6JCZE8Q" # TS Command Read Key
WRITE_KEY="IOOAC36UJI0C2JFI" # TS History Write Key

##Date and Time
gino= datetime.datetime.now()
D=(str(gino.year)+'-'+str(gino.month)+'-'+str(gino.day))
T=(str(gino.hour)+':'+str(gino.minute)+':'+str(gino.second))

def getTime():
    global gino
    global D
    global T
    gino= datetime.datetime.now()
    D=(str(gino.year)+'-'+str(gino.month)+'-'+str(gino.day))
    T=(str(gino.hour)+':'+str(gino.minute)+':'+str(gino.second))
    
##Global Variables
isArmed=0
motionIsOn=0
flameIsOn=0
lockIsOn=0
cameraIsOn=0
buzzerIsOn=0

##Main function running the system
def main():
    configSystem()
    while True:
        getTime()
        updateStatus()
        lock(lockIsOn)
        if isArmed == 1:
            print(lock(lockIsOn))
            if motionDetect(motionIsOn) == 1:
                takeAction(0) 
            if flameDetect(flameIsOn) == 1:
                takeAction(1)
        time.sleep(1)

##Configuring the System
def configSystem():
    configMotion()
    configFlame()
    configLock()
    configBuzzer()
    return 1

##Updating the sensor's status from the thingSpeak command channel       
def updateStatus():
    global isArmed
    global lockIsOn
    global cameraIsOn
    global buzzerIsOn
    global motionIsOn
    global flameIsOn
    curr_status=thingspeak_read_c(READ_KEY,ID)
    isArmed=int(curr_status[0])
    lockIsOn=int(curr_status[1])
    cameraIsOn=int(curr_status[2])
    buzzerIsOn=int(curr_status[3])
    motionIsOn=int(curr_status[4])
    flameIsOn=int(curr_status[5])
    return 1

##Take action function        
def takeAction(sensor):
    if sensor==0:
#         print("Motion Detected!!")
        recordVideo(cameraIsOn)
        buzz(buzzerIsOn)
        updateHistory(0, cameraIsOn)
        return 1
    elif sensor==1:
#         print("Fire Detected!!")
        buzz(buzzerIsOn)
        recordVideo(cameraIsOn)
        updateHistory(1, cameraIsOn)
        return 1
    else:
        return 0

##Updating the history thingspeak upon the occurence of an event    
def updateHistory(sensor,cameraIsOn):
    if sensor==0 and cameraIsOn==0:   
        sen="Motion"
        thingspeak_write_h(ID, D, T, sen, "NA", WRITE_KEY)
        return 1
    elif sensor==1 and cameraIsOn==0:
        sen="Flame"
        thingspeak_write_h(ID, D, T, sen, "NA", WRITE_KEY)
        return 1
    elif sensor==0 and cameraIsOn==1:
        sen="Motion"
        thingspeak_write_h(ID, D, T, sen, '/home/pi/Desktop/security', WRITE_KEY)
        return 1
    elif sensor==1 and cameraIsOn==1:
        sen="Flame"
        thingspeak_write_h(ID, D, T, sen, '/home/pi/Desktop/security', WRITE_KEY)
        return 1
    else:
        return 0
        
def recordVideo(cameraIsOn):
    cock=str(gino)
    if cameraIsOn==1:
        with picamera.PiCamera() as camera:
            camera.resolution=(1280, 720)
            camera.rotation = (180)
            camera.start_preview(alpha=192)
            camera.start_recording('/home/pi/Desktop/security/{}.h264'.format(gino))
            time.sleep(5)
            camera.stop_preview()
            camera.stop_recording()
        return 1
    elif cameraIsOn==0:
        return 1
    else:
        return 0

##Run the main
def startup():
    x = int(input("To start system press 1/ Press 0 to quit: "))
    if x==1:
        main()
    else:
        print("bye")
startup()