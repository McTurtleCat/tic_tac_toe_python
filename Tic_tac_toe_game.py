#Tic tac toe game

def PrintBoardKey (BoardDictionaryKey):
    print( "|", BoardDictionaryKey["TopLeft"],    "|", BoardDictionaryKey["TopCentre"],    "|", BoardDictionaryKey["TopRight"],     "|" )
    print( "|", BoardDictionaryKey["MiddleLeft"], "|", BoardDictionaryKey["MiddleCentre"], "|", BoardDictionaryKey["MiddleRight"],  "|" )
    print( "|", BoardDictionaryKey["BottomLeft"], "|", BoardDictionaryKey["BottomCentre"], "|", BoardDictionaryKey["BottomRight"] , "|\n")

    print("To enter a value into a square enter the 2 letters in the square in the same order.""\n")

def PrintBoard (BoardDictionary):
    print( "|", BoardDictionary["TopLeft"],    "|", BoardDictionary["TopCentre"],    "|", BoardDictionary["TopRight"],     "|" )
    print( "|", BoardDictionary["MiddleLeft"], "|", BoardDictionary["MiddleCentre"], "|", BoardDictionary["MiddleRight"],  "|" )
    print( "|", BoardDictionary["BottomLeft"], "|", BoardDictionary["BottomCentre"], "|", BoardDictionary["BottomRight"] , "|\n")


import random
RandNumber = random.randint(1,2)
#print(RandNumber)

if RandNumber == 1:
    Turn = "X"

elif RandNumber == 2:
    Turn = "O"

else:
    print("Error")

#   ----MAIN PORGRAM-----

BoardDictionaryKey = {"TopLeft":"TL","TopCentre":"TC", "TopRight":"TR", "MiddleLeft":"ML","MiddleCentre":"MC", "MiddleRight":"MR", "BottomLeft":"BL","BottomCentre":"BC", "BottomRight":"BR"}
BoardDictionary = {"TopLeft":"","TopCentre":"", "TopRight":"", "MiddleLeft":"","MiddleCentre":"", "MiddleRight":"", "BottomLeft":"","BottomCentre":"", "BottomRight":""}



PrintBoardKey (BoardDictionaryKey)

print("It is" , Turn , "'s Turn\n ")

#PrintBoard (BoardDictionary)