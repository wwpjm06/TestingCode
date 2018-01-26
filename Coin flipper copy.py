## Coin flipper

import random

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
# End of def +++++++++++++++++++++

## Set number of flips to a FALSE value
iMax="Q"

sCarryOn="C"
while sCarryOn == "C":
    while RepresentsInt(iMax) == False and sCarryOn == "C":
        iMax = input("\nEnter number of flips ")
    #End of RepresentsInt While

    # initialise variables
    iCount = 0
    iHeads = 0
    iTails = 0
    iMax = int(iMax)
    while iCount < iMax:
        # print("Flipping coin")
        # Set random number
        iNum = random.randint(1,2)
#        iNum = random.randint(1,3)
        if iNum == 1:
            iHeads += 1
        elif iNum == 2:
            iTails += 1
        else:
            print("Invalid number ",iNum)
        iCount += 1
    #End of iCount While

    print("\n\nOf " + str(iCount) + " flips there were "+ str(iHeads) + " Heads and "+ str(iTails) + " Tails")
    iMax="Q"
    sCarryOn=input("\nPress c <<then Enter>> to Continue or any other key <<then Enter>> to Exit >>>>>>\n\n").upper()
#End of CarryOn While
print("Program terminated as you pressed \"" + sCarryOn +"\"")
