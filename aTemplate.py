# Template program

import RPi.GPIO as GPIO
import time



sCarryOn="C"
while sCarryOn == "C":




    
    sCarryOn=input("\nPress c <<then Enter>> to Continue or any other key <<then Enter>> to Exit >>>>>>\n\n").upper()
#End of CarryOn While
print("Program terminated as you pressed the key\"" + sCarryOn +"\"")
