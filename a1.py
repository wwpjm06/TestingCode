# Template program

c=1

sCarryOn="C"
while sCarryOn == "C":

    while c <= 100:
        print(str(c))
        c+=1


    
    sCarryOn=input("\nPress c <<then Enter>> to Continue or any other key <<then Enter>> to Exit >>>>>>\n\n").upper()
#End of CarryOn While
print("Program terminated as you pressed \"" + sCarryOn +"\"")
