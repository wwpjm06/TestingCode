# Program to buy/redeem Character Attributes
# Plyer can buy/sell BUT can't own more than x1 Attribute OR all Attributes

sCarryOn="C"
while sCarryOn == "C":

    CharAtts=[("Dexterity",14),("Health",10),("Strength",8),("Wisdom",12)]
    MaxPoints=30
    menuOpt=None
    
    # Print menu
    print("""

         This is the Menu

         0=Exit
         1=Buy Attributes
         2=Redeem Attributes
         3=List Attributes

         """)
    while menuOpt !=0:

        menuOpt=input("What slection do you want?")

        if menuOpt == 1:
            print("Option 1")
        elif menuOpt == 2:
            print("Option 2")
        elif menuOpt == 3:
            print("Option 3")
#        elif menuOpt == 0:
#            print("Option 0")
            # Break out
#        else:
#            print("Not a valid option\n\n")
    



    sCarryOn=input("\nPress c <<then Enter>> to Continue or any other key <<then Enter>> to Exit >>>>>>\n\n").upper()
#End of CarryOn While
print("Program terminated as you pressed \"" + sCarryOn +"\"")
