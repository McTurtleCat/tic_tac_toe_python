'''
Tic tac toe game.

Implementation of the tic-tac-toe game, otherwise known as X's and O's. This is
a command line game that accepts text input and generates text output.
'''


# Import to support enumerations
from enum import Enum


class Square(Enum):
    '''
    Enumeration to define the options for each square of the board.
    '''

    EMPTY = 0
    X = 1
    O = 2


class Board:
    '''
    Class for current state of the board.

    Attributes:
        NumOfRows (int): Number of rows in the board (i.e the vertical size).
        NumOfCols (int): Number of columns in the board (i.e the horizonal size)
        NumOfSquares (int): Total number of squares on the board
    '''

    NumOfRows = 3  # Set to the standard board size
    NumOfCols = NumOfRows  # Make the board square
    NumOfSquares = NumOfRows * NumOfCols
    Squares = [Square.EMPTY] * NumOfSquares  # Create an empty board


    def ListIndex(self, row, col):
        '''
        Translate a board pointion to an index of the board squares list.

        Args:
            row (int): Vertical position of the board square (0 based).
            col (int): Horizontal position of the board square (0 based).

        Returns:
            int: Index of the specified square in the boards squares list.
        '''

        return ((row * self.NumOfRows) + col)


    def SetSquare(self, row, col, square):
        '''
        Set a specific square to a specified value.

        Set a square on the board, specified by row and column, to a specified
        value.

        Args:
            row (int): Vertical position of the board square (0 based).
            col (int): Horizontal position of the board square (0 based).
            square (Square): Current state of the specified board position.
        '''

        SquareListPosition = self.ListIndex(col, row)
        self.Squares[SquareListPosition] = square


    def GetSquare(self, row, col):
        '''
        Retrive the value of a specific square by using the position (row/column)

        Args:
            row (int): Vertical position of the board square (0 based).
            col (int): Horizontal position of the board square (0 based).

        Returns:
            Square: Current state of the specified board position.
        '''

        SquareListPosition = self.ListIndex(col, row)

        return self.Squares[SquareListPosition] 


    def DisplayBoard(self):
        '''
        Displays the board
        Has a dictionary to assign enumeration values to their character representation
        Repeats while displaying the values for all squares row by row
        Creates a new line at the end of each row
        '''

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
    '''
    Run the board tests
    '''
    print("Tic tac toe game")

    board = Board()  # Create a new board
    board.DisplayBoard()

    # Testing: Set a specific square on the board to a known value
    board.SetSquare(2, 1, Square.X)

    board.DisplayBoard()  # Display the updated board

    # Testing: Getting a specific square from the board 
    square = board.GetSquare(2, 1)

    #If the value the function returns is the same as the value set,
    # then it displays a success message
    if (square == Square.X):
        print("Success")

    # Overwise it displays the message Failure, 
    # while also displaying the value the function found
    else:
        print("Failure (found ", square, ")")


# Entry point for the program, if run as a script
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