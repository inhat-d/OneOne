### Info
# Sorry for this strange strokes and maybe some mistakes, now it is 11:32 PM. I need a nap :(
#
# Are you watched "Infinite Train" serial? No? SO WATCH - IT'S SO BEAUTIFULKK. Khem... Nevermind...
# This project is replica of OneOne, the double-minded robot. 
#
# YOU NEED TO INSERT YOUR OWN API. NO FREE API HERE >:(
#
###



### The Import Part.

from openai import OpenAI

import minds.theOneHappy as THO
import minds.theOneSad as TSO

import random as rn
import time as tm

###



### We need to chose!!!

ask = input("Ask OneOne something > ")
OneOne = rn.randint(1, 3)

###



### The "If-Then" Part.

if OneOne == 1:    #TheHappyOne
    print("God of randomnes desided that theHappyOne will answer you.")
    tm.sleep(3)
    THO.callhappy(prompt=ask)

elif OneOne == 2:    #TheSadOne
    print("God of randomnes desided that theSadOne will answer you.")
    tm.sleep(3)
    TSO.callsad(prompt=ask)

elif OneOne == 3:    #Both
    print("You extremly lucky, and both minds of OneOne will answer you")
    tm.sleep(3)
    
    print("")
    print("TheHappyOne:")
    THO.callhappy(prompt=ask)

    tm.sleep(3)
    print("")
    print("TheSadOne:")
    TSO.callsad(prompt=ask)

###



### Bye!

for x in range(1, 4):
    print("")

print("I hope you find your answer. Bye!")
