import RPi.GPIO as GPIO
import time

channel = 7

def configLock():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(7, GPIO.LOW)
    return 1
    
def lock(lockIsOn):
    if lockIsOn==1:
        GPIO.output(7, GPIO.HIGH)
        return 1
    elif lockIsOn==0:
        GPIO.output(7, GPIO.LOW)
        return 1
    else:
        return 0
    