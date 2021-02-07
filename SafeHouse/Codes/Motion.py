import RPi.GPIO as GPIO
import time

channel = 40

def configMotion():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.IN)
    return 1

def motionDetect(motionIsOn)-> int:
    if motionIsOn==1:
        if GPIO.input(channel)==1:
            return 1
        else:
            return 0
    elif motionIsOn==0:
        return 2
    else:
        return 0