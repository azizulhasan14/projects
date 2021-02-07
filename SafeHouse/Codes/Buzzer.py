import RPi.GPIO as GPIO
import time

channel = 38

def configBuzzer():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.LOW)
    return 1
    
def buzz(buzzerIsOn):
    if buzzerIsOn==1:
        GPIO.output(channel, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(channel, GPIO.LOW)
        return 1
    elif buzzerIsOn==0:
        return 1
    else:
        return 0
