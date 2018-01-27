# Program to buy/redeem Character Attributes C5.C2
# Plyer can buy/sell BUT can't own more than x1 Attribute OR all Attributes

sCarryOn="C"
while sCarryOn == "C":

    CHARATTS={"Dexterity" : 14,
              "Health" : 10,
              "Strength" : 8,
              "Wisdom" : 12}

    ExistAtts={}
    MaxPoints=30
    menuOpt=None
    AttribItem=None
    
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
            
            AttribItem=input("Which attribute do you wish to buy? ")

            if AttribItem in ExistAtts:
                print("You already have " + AttribItem)
            else:
#                print("\n"+ str(.get(AttribItem)) + " : " + str(CurPoints))
                if AttribItem in CHARATTS:
                    if MaxPoints >= CHARATTS.get(AttribItem):
                        
                        # Add Attribute to Directory ExistAtts
                        ExistAtts[AttribItem] = CHARATTS.get(AttribItem)
                        print("You now own " + str(ExistAtts))

                        # Deduct points from MaxPoints
                        MaxPoints -= CHARATTS.get(AttribItem)

                    else:
                        if MaxPoints == 0:
                            print("You don't have any points left")
                        else:
    #                        print("You only have "+str(MaxPoints))
                            print("You don't have enough points")
                else:
                    print("\n"+AttribItem + " doesn't exist")
        # End of Option 1
        elif menuOpt == 2:
            print("You own " + str(ExistAtts))
            AttribItem=input("Which attribute do you wish to sell? ")
            if AttribItem in ExistAtts:
                    
                # Add points to MaxPoints
                MaxPoints += ExistAtts.get(AttribItem)

                # Remove Attribute from Directory ExistAtts
                del ExistAtts[AttribItem]
                print("You now own " + str(ExistAtts))
            else:
                print("You don't own " + AttribItem)
        # End of Option 2
        elif menuOpt == 3:
            print("Option 3 - List Attributes\n")
            print("You own " + str(ExistAtts)+"\n")
        else:
            if menuOpt != 0 :print("Not a valid option\n\n")




    sCarryOn=input("\nPress c <<then Enter>> to Continue or any other key <<then Enter>> to Exit >>>>>>\n\n").upper()
#End of CarryOn While
print("Program terminated as you pressed \"" + sCarryOn +"\"")
