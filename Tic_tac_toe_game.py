'''
Tic tac toe game.

Implementation of the tic-tac-toe game, otherwise known as X's and O's. This is
a command line game that accepts text input and generates text output.
'''


# Import to support enumerations
from enum import Enum

import random


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

    def ListIndexInverse(self, IndexNumber):
            '''
            Translate a index of the board squares list to a board pointion in 
            columns and rows.
    
            Args:
                IndexNumber (int):Index of board squares
    
            Returns:
                row (int): Vertical position of the board square (0 based).
                col (int):Horizontal position of the board square (0 based).
            '''

            col = IndexNumber % self.NumOfCols
            row = int(IndexNumber/self.NumOfCols)

            return row,col


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

    def GameWin(self, square):
        '''
        Check the board to determine whether the specified square has a winning position. 
        A winning position is one where one of the following is true:
                  * a row where all the squares in the row are the same
                  * a column where all the squares in the column are the same
                  * or a diaganol from the top left to bottom right
                  * or a diagonial from the top right to bottom left

        Args:
            square (Square): Current state of the specified board position.
        '''

        Win = False


        #Columns
        Win = Win or \
            (self.GetSquare(0, 0) == self.GetSquare(1, 0) == self.GetSquare(2, 0) == square) or \
            (self.GetSquare(0, 1) == self.GetSquare(1, 1) == self.GetSquare(2, 1) == square) or \
            (self.GetSquare(0, 2) == self.GetSquare(1, 2) == self.GetSquare(2, 2) == square)

        #rows
        Win = Win or \
            (self.GetSquare(0, 0) == self.GetSquare(0, 1) == self.GetSquare(0, 2) == square) or \
            (self.GetSquare(1, 0) == self.GetSquare(1, 1) == self.GetSquare(1, 2) == square) or \
            (self.GetSquare(2, 0) == self.GetSquare(2, 1) == self.GetSquare(2, 2) == square)

        #diagonals
        Win = Win or\
            (self.GetSquare(0, 0) == self.GetSquare(1, 1) == self.GetSquare(2, 2) == square) or\
            (self.GetSquare(0, 2) == self.GetSquare(1, 1) == self.GetSquare(2, 0) == square)


        return Win

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
            SquareCharacter = SquareDictionary[square]
            print(SquareCharacter, end="")


            if Index % self.NumOfCols == 0:
                print()

class Player:

    def Turn():

        RandNumber = random.randint(1,2)
        Number = RandNumber % 2

        if Number == 1:
            Letter = "X"

        elif Number == 0:
            Letter = "O"

        Number += 1

        Number = Number % 2

        print("It is's" ,Letter, " Turn\n ")

    def Move(board):

        BoardDictionaryKey = {"TopLeft":0,"TopCentre":3, "TopRight":6, "MiddleLeft":1,"MiddleCentre":4, "MiddleRight":7, "BottomLeft":2,"BottomCentre":5, "BottomRight":8}
        print ("Input one of the following squares, Key: TopLeft, TopCentre, TopRight, MiddleLeft, MiddleCentre, MiddleRight, BottomLeft, BottomCentre, BottomRight")
        SquareInput = input("What square do you want to input? ")

        while SquareInput not in BoardDictionaryKey:

            print("error,please re-enter")
            SquareInput = input("What square do you want to input? ")
        
        row,col = board.ListIndexInverse (BoardDictionaryKey[SquareInput])



        board.SetSquare(row, col, Square.X)
        board.DisplayBoard()



def main():
    '''
    Run the board tests
    '''

    print("Tic tac toe game")

    board = Board()  # Create a new board
    board.DisplayBoard()

    # Testing: Set a specific square on the board to a known value
    board.SetSquare(0, 1, Square.X)

    board.DisplayBoard()  # Display the updated board

    # Testing: Getting a specific square from the board 
    square = board.GetSquare(0, 1)

    #If the value the function returns is the same as the value set,
    # then it displays a success message
    if (square == Square.X):
        print("Success")

    # Overwise it displays the message Failure, 
    # while also displaying the value the function found
    else:
        print("Failure (found ", square, ")")

    board.SetSquare(0, 2, Square.X)  # Testing: Set a specific square on the board to a known value
    board.SetSquare(0, 0, Square.X)  # Testing: Set a specific square on the board to a known value
    board.DisplayBoard()


    Win = board.GameWin(Square.X) # Calling the GameWin function to see if the Game has been won
    board.DisplayBoard()

    #print(Win) #Testing: to see if win is true or false
    if Win == True:
        print("The game has been won by X")


    board.SetSquare(0, 1, Square.EMPTY)
    board.SetSquare(0, 2, Square.EMPTY)
    board.SetSquare(0, 0, Square.EMPTY)
    board.DisplayBoard()

    Player.Turn ()

    TestIndex = board.ListIndex(2,1)
    Horiz,Vert = board.ListIndexInverse(TestIndex)

    if Horiz == 2 and Vert == 1:
        print("ListIndexInverse Test Passed")

    Player.Move(board)

# Entry point for the program, if run as a script
if __name__ == "__main__":
    main()