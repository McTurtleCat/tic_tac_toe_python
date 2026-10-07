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
            SquareCharacter = SquareDictionary[square]
            print(SquareCharacter, end="")


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