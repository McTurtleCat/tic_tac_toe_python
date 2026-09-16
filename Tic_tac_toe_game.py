#Tic tac toe game

#Board the users play on
def PrintBoard (BoardDictionary):
    print( "|", BoardDictionary["TopLeft"],    "|", BoardDictionary["TopCentre"],    "|", BoardDictionary["TopRight"],     "|" )
    print( "|", BoardDictionary["MiddleLeft"], "|", BoardDictionary["MiddleCentre"], "|", BoardDictionary["MiddleRight"],  "|" )
    print( "|", BoardDictionary["BottomLeft"], "|", BoardDictionary["BottomCentre"], "|", BoardDictionary["BottomRight"] , "|\n")

def Turn(Number):

    if Number == 1:
        Letter = "X"

    elif Number == 0:
        Letter = "O"

    Number += 1
    #print(Number)
    Number = Number % 2
    #print(Number)

    print("It is" , Letter , "'s Turn\n ")

#   ----MAIN PORGRAM-----

import random
RandNumber = random.randint(1,2)
 #print(RandNumber)

Number = RandNumber % 2
#print(Number)

#Dictionary for the boxs with different key values for each one (values are NOT changed)
BoardDictionaryKey = {"TopLeft":"TL","TopCentre":"TC", "TopRight":"TR", "MiddleLeft":"ML","MiddleCentre":"MC", "MiddleRight":"MR", "BottomLeft":"BL","BottomCentre":"BC", "BottomRight":"BR"}

#Dictionary for the board, which is used by the player, begins with no values, as the game progresses the keys in the dictionary get values
BoardDictionary = {"TopLeft":"","TopCentre":"", "TopRight":"", "MiddleLeft":"","MiddleCentre":"", "MiddleRight":"", "BottomLeft":"","BottomCentre":"", "BottomRight":""}

PrintBoard (BoardDictionaryKey)

Turn (Number)

#PrintBoard (BoardDictionary)