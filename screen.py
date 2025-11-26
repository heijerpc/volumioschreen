import RPi.GPIO as GPIO
from time import sleep 
import subprocess


GPIO.setwarnings(False)                # allow use of pin within multiple script
GPIO.setmode(GPIO.BOARD)               # use pinnumbers of board
GPIO.setup(11, GPIO.IN)                 # define input port / turn screen off
GPIO.setup(13, GPIO.IN)                 # define input port / turn screen on 


while True:                              # 
    if GPIO.input(11) == 0:              # turning screen off 
        subprocess.run(['volumio pause']) 
        subprocess.run(['xset dpms force off'])
        print("screen is turned off") 
        sleep(1)

    if GPIO.input(13) == 0:              # turn screen on 
        subprocess.run(['volumio play']) 
        subprocess.run(['xset dpms force on'])
        print("screen is turned on")
        sleep(1)