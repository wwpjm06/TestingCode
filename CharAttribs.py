# Program to buy/redeem Character Attributes C5.C2
# Plyer can buy/sell BUT can't own more than x1 Attribute OR all Attributes

sCarryOn="C"
while sCarryOn == "C":

    CHARATTS={"Dexterity" : 14,
              "Health" : 10,
              "Strength" : 8,
              "Wisdom" : 12}

    ExistAtts={"Health" : 10,
              "Strength" : 8,
              "Wisdom" : 12}

    MaxPoints=0
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
            print("You own " + str(ExistAtts) + "\n")
            if MaxPoints == 0:
                print("\nYou don't have any points to buy anything\n")
            else:
                print("\nYou have " + str(MaxPoints) + " points to buy " + str(CHARATTS) + "\n")
                
                AttribItem=input("Which attribute do you wish to buy? ")

                if AttribItem in ExistAtts:
                    print("You already have " + AttribItem)
                else:
                    # Check that AttribItem *IS* in the Directory
                    if AttribItem in CHARATTS:
                        # Make sure there are enough points to buy attribute
                        if MaxPoints >= CHARATTS.get(AttribItem):
                            # Add Attribute to Directory ExistAtts
                            ExistAtts[AttribItem] = CHARATTS.get(AttribItem)

                            # Display what is owned
                            print("You now own " + str(ExistAtts))

                            # Deduct points from MaxPoints
                            MaxPoints -= CHARATTS.get(AttribItem)

                        else:
                            if MaxPoints == 0:
                                print("You don't have any points left")
                            else:
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

                # Display what is owned
                print("You now own " + str(ExistAtts))
            else:
                print("You don't own " + AttribItem)
        # End of Option 2
        
        elif menuOpt == 3:
            print("Option 3 - List Attributes\n")
            print("You own " + str(ExistAtts)+"\n")
        # End of Option 3
        else:
            if menuOpt != 0 :print("Not a valid option\n\n")

    # End of WHILE loop



    sCarryOn=input("\nPress c <<then Enter>> to Continue or any other key <<then Enter>> to Exit >>>>>>\n\n").upper()
#End of CarryOn While
print("Program terminated as you pressed \"" + sCarryOn +"\"")
