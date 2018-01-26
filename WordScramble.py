# This program will take a list of words and then scramble the up
# Chapter 5 Challenge 1


import random

word=None
WORDS=[]

sCarryOn="C"
while sCarryOn == "C":

    WORDS = ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel"]

    while len(WORDS) !=0:
        word=random.choice(WORDS)
        WORDS.remove(word)
        print(word)
#        print("\n"+word+"\n")
#        print(WORDS)

    # End of len(WORDS) while    


    
    sCarryOn=input("\nPress c <<then Enter>> to Continue or any other key <<then Enter>> to Exit >>>>>>\n\n").upper()
#End of CarryOn While
print("Program terminated as you pressed \"" + sCarryOn +"\"")
