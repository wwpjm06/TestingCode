# Program to buy/redeem Character Attributes
# Plyer can buy/sell BUT can't own more than x1 Attribute OR all Attributes

sCarryOn="C"
while sCarryOn == "C":

    CharAtts={"Dexterity" : 14,
              "Health" : 10,
              "Strength" : 8,
              "Wisdom" : 12}
    
    ExistAtts={}
    MaxPoints=30
#    CurPoints = 0
    menuOpt=None
    AddAttrib=None
    
    # Print menu
    print("""

         This is the Menu

         0=Exit
         1=Buy Attributes
         2=Redeem Attributes
         3=List Attributes

         """)
    while menuOpt !=0:

        menuOpt=int(input("What selection do you want? :"))

        
        if menuOpt == 1:
            print("Option 1")
            AddAttrib=input("Which attribute do you wish to buy? ")
            
            if AddAttrib in ExistAtts:
                print("You already have " + AddAttrib)
            else:
#                print("\n"+ str(CharAtts.get(AddAttrib)) + " : " + str(CurPoints))
                if MaxPoints >= CharAtts.get(AddAttrib):
                    print("We'll add " + AddAttrib)
                    ExistAtts[AddAttrib] = CharAtts.get(AddAttrib)
                    print("You now have " + str(ExistAtts))
                    MaxPoints -= CharAtts.get(AddAttrib)
                    print("You now have " + str(MaxPoints) + " left")
                else:
                    if MaxPoints == 0:
                        print("You don't have any points left")
                    else:
                        print("You only have "+str(MaxPoints))
                    
        elif menuOpt == 2:
            print("Option 2")
        elif menuOpt == 3:
            print("Option 3")
        else:
            print("Not a valid option\n\n")
    



    sCarryOn=input("\nPress c <<then Enter>> to Continue or any other key <<then Enter>> to Exit >>>>>>\n\n").upper()
#End of CarryOn While
print("Program terminated as you pressed \"" + sCarryOn +"\"")
