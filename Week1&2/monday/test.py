from random import*
Randomnumber= randint(1,20)

guessnum= False

i=0
while i<3:
    guess = input("Guess number from 1 to 20")
    if not guess.isnumeric():
         print(" That is not a positive whole number")
    else
