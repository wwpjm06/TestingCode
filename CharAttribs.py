# Program to buy/redeem Character Attributes
# Plyer can buy/sell BUT can't own more than x1 Attribute OR all Attributes

sCarryOn="C"
while sCarryOn == "C":

    CHARATTS={"Dexterity" : 14,
              "Health" : 10,
              "Strength" : 8,
              "Wisdom" : 12}

    ExistAtts={}
    MaxPoints=30
#    CurPoints = 0
    menuOpt=None
    AddAttrib=None
    
    while menuOpt !=0:

        # Print menu
        print("""

             Character Attributes Menu
             =========================

             0=Exit
             1=Buy Attributes
             2=Redeem Attributes
             3=List Attributes

             """)
    
        print("\nYou have " + str(MaxPoints) + " points\n")
        menuOpt=int(input("What selection do you want? :"))


        if menuOpt == 1:
            print("\nYou have " + str(MaxPoints) + " points to buy " + str(CHARATTS) + "\n")
            print("You own " + str(ExistAtts) + "\n")
            
            AddAttrib=input("Which attribute do you wish to buy? ")

            if AddAttrib in ExistAtts:
                print("You already have " + AddAttrib)
            else:
#                print("\n"+ str(.get(AddAttrib)) + " : " + str(CurPoints))
                if AddAttrib in CHARATTS:
                    if MaxPoints >= CHARATTS.get(AddAttrib):
                        
                        # Add Attribute to Directory ExistAtts
                        ExistAtts[AddAttrib] = CHARATTS.get(AddAttrib)
                        print("You now own " + str(ExistAtts))

                        # Deduct points from MaxPoints
                        MaxPoints -= CHARATTS.get(AddAttrib)

                    else:
                        if MaxPoints == 0:
                            print("You don't have any points left")
                        else:
    #                        print("You only have "+str(MaxPoints))
                            print("You don't have enough points")
                else:
                    print("\n"+AddAttrib + " doesn't exist")
        # End of Option 1
        elif menuOpt == 2:
            print("You own " + str(ExistAtts))
            AddAttrib=input("Which attribute do you wish to sell? ")
            if AddAttrib in ExistAtts:
                    
                # Add points to MaxPoints
                MaxPoints += ExistAtts.get(AddAttrib)

                # Remove Attribute from Directory ExistAtts
                del ExistAtts[AddAttrib]
                print("You now own " + str(ExistAtts))
            else:
                print("You don't own " + AddAttrib)
        # End of Option 2
        elif menuOpt == 3:
            print("Option 3 - List Attributes\n")
            print("You own " + str(ExistAtts)+"\n")
        else:
            if menuOpt != 0 :print("Not a valid option\n\n")




    sCarryOn=input("\nPress c <<then Enter>> to Continue or any other key <<then Enter>> to Exit >>>>>>\n\n").upper()
#End of CarryOn While
print("Program terminated as you pressed \"" + sCarryOn +"\"")
