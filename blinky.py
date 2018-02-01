# Template program

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

sCarryOn="C"
while sCarryOn == "C":

    
# loop through 50 times, on/off for 1 second
    for i in range(50):
        GPIO.output(7,True)
        time.sleep(1)
        GPIO.output(7,False)
        time.sleep(1)
    GPIO.cleanup()



    
    sCarryOn=input("\nPress c <<then Enter>> to Continue or any other key <<then Enter>> to Exit >>>>>>\n\n").upper()
#End of CarryOn While
print("Program terminated as you pressed \"" + sCarryOn +"\"")
