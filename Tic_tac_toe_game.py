#Tic tac toe game
from enum import Enum

class Square(Enum):
    EMPTY = 0
    X = 1
    O = 2


class Board:
    NumOfRows = 3
    NumOfCols = NumOfRows
    NumOfSquares = NumOfRows * NumOfCols

    Squares = [Square.EMPTY] * NumOfSquares

    def DisplayBoard(self):

        SquareDictionary = {
            Square.EMPTY: ".", 
            Square.X: "X", 
            Square.O: "O"
        }

        print("___")

        for Index, square in enumerate(self.Squares, start=1):
            square_character = SquareDictionary[square]
            print(square_character, end="")

            if Index % self.NumOfCols == 0:
                print()


def main():
    print("Tic tac toe game")
    board = Board()
    board.DisplayBoard()


if __name__ == "__main__":
    main()

          
"""""
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
print("To enter a value in a square enter the two correspounding letters""\n")


Turn (Number)

#PrintBoard (BoardDictionary)


# -- Inputs --
WinCondition = False

while WinCondition == False or (BoardDictionary["TopLeft"] == "" and BoardDictionary["TopCentre"] == "" and BoardDictionary["TopRight"] == "" and BoardDictionary["MiddleLeft"] == "" and BoardDictionary["MiddleCentre"] == "" and BoardDictionary["MiddleRight"] == "" and BoardDictionary["BottomLeft"] == "" and BoardDictionary["BottomCentre"] == "" and BoardDictionary["BottomRight"] == ""):

    UserInput = input("What square do you want to input ").upper()
    #print(UserInput)

    if UserInput == "HELP":
        print("")
        PrintBoard(BoardDictionaryKey)
        print("To enter a value in a square enter the two correspounding letters""\n")


    while UserInput != "TL" and UserInput != "TC" and UserInput != "TR" and UserInput != "ML" and UserInput != "MC" and UserInput != "MR" and UserInput != "BL" and UserInput != "BC" and UserInput != "BR":
        UserInput = input("Error please re-enter what square you want to input ").upper()

        if UserInput == "HELP":
                print("")
                PrintBoard(BoardDictionaryKey)
                print("To enter a value in a square enter the two correspounding letters""\n")
"""