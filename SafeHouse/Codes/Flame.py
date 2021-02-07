import RPi.GPIO as GPIO
import time

channel = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)

def configFlame():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.IN)
    return 1


def flameDetect(flameIsOn) -> int:
    if flameIsOn==1: #GPIO could be high
            if GPIO.input(channel)==0:          
                return 1
            else:
                return 0
    elif flameIsOn==0:
        return 2
    else:
        return 0
