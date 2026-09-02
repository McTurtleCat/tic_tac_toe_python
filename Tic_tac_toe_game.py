#Tic tac toe game

def PrintBoard (BoardDictionary):
    print( "|", BoardDictionary["TopLeft"],    "|", BoardDictionary["TopCentre"],    "|", BoardDictionary["TopRight"],     "|" )
    print( "|", BoardDictionary["MiddleLeft"], "|", BoardDictionary["MiddleCentre"], "|", BoardDictionary["MiddleRight"],  "|" )
    print( "|", BoardDictionary["BottomLeft"], "|", BoardDictionary["BottomCentre"], "|", BoardDictionary["BottomRight"] , "|\n")

#Main
import random
RandNumber = random.randint(1,2)
#print(RandNumber)

if RandNumber == 1:
    Turn = "X"

elif RandNumber == 2:
    Turn = "O"

else:
    print("Error")

BoardDictionary = {"TopLeft":"TL","TopCentre":"TC", "TopRight":"TR", "MiddleLeft":"ML","MiddleCentre":"MC", "MiddleRight":"MR", "BottomLeft":"BL","BottomCentre":"BC", "BottomRight":"BR"}

PrintBoard (BoardDictionary)
print("To enter a value into a square enter the 2 letters in the square in the same order.")

print("It is" , Turn , "'s Turn\n ")

