import RPi.GPIO as GPIO
from time import sleep 
import subprocess
import os


GPIO.setwarnings(False)                # allow use of pin within multiple script
GPIO.setmode(GPIO.BOARD)               # use pinnumbers of board
GPIO.setup(11, GPIO.IN)                 # define input port / turn screen off
GPIO.setup(13, GPIO.IN)                 # define input port / turn screen on 

os.environ['DISPLAY'] = ':0'

print("screen on / screen off is running") 

while True:                              # 
    if GPIO.input(11) == 1:              # turning screen off 
#        os.system('xset dpms force off')
        subprocess.run('xset dpms force off', shell = True)
        print("screen is turned off") 
        sleep(1)

    if GPIO.input(13) == 1:              # turn screen on 
 #       os.system('xset dpms force on')
        subprocess.run("volumio play",shell=True) 
        subprocess.run('xset dpms force on',shell=True)
        print("screen is turned on")
        sleep(1)