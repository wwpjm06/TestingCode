# Testing program for JQC-3FF-=S-Z relay 

import RPi.GPIO as GPIO
#import time
from time import sleep

LEDPin = 17
i=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPin,GPIO.OUT)

#sCarryOn="C"
#while sCarryOn == "C":

try:
    # here you put your main loop or block of code  
    # loop through 50 times, on/off for 1 second
    #for i in range(10):
    print("Before set Pin")
    GPIO.output(LEDPin,True)
    print("After set Pin")
    #time.sleep(15)
    while i <=5000:
        i+=1
        print(str(i))
    #sleep(5)
    print("After Sleep time")
     #       GPIO.output(LEDPin,False)
     #       time.sleep(1)
  
except KeyboardInterrupt:  
    # here you put any code you want to run before the program
    print("Keyboard Interrupt")
     # exits when you press CTRL+C  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print("Other error or exception occurred!")  
  
finally:  
   GPIO.cleanup() # this ensures a clean exit
print(" - after Cleanup")



    
    #sCarryOn=input("\nPress c <<then Enter>> to Continue or any other key <<then Enter>> to Exit >>>>>>\n\n").upper()
#End of CarryOn While
#print("Program terminated as you pressed \"" + sCarryOn +"\"")
