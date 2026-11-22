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
        NumOfCols (int): Number of columns in the board (i.e the horizontal size)
        NumOfSquares (int): Total number of squares on the board
    '''

    NumOfRows = 3  # Set to the standard board size
    NumOfCols = NumOfRows  # Make the board square
    NumOfSquares = NumOfRows * NumOfCols
    Squares = [Square.EMPTY] * NumOfSquares  # Create an empty board


    def ListIndex(self, row, col):
        '''
        Translate a board position to an index of the board squares list.

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
        Retrieve the value of a specific square by using the position (row/column)

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
                  * or a diagonal from the top left to bottom right
                  * or a diagonal from the top right to bottom left

        Args:
            square (Square): Current state of the specified board position.

        Return:
            Win (Boolean): Decides if a winning position has been achieved 
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

    def Draw(self):
        '''
        Checks to see if the game is a draw
        The game is a draw when all squares have a value (Either X or O)

        Return:
            Draw (Boolean): Decides if a draw requirements have been met.
        '''

        Draw = False

        Draw = Draw or\
            (self.GetSquare (0, 0) != Square.EMPTY) and \
            (self.GetSquare (0, 1) != Square.EMPTY) and \
            (self.GetSquare (0, 2) != Square.EMPTY) and \
            (self.GetSquare (1, 0) != Square.EMPTY) and \
            (self.GetSquare (1, 1) != Square.EMPTY) and \
            (self.GetSquare (1, 2) != Square.EMPTY) and \
            (self.GetSquare (2, 0) != Square.EMPTY) and \
            (self.GetSquare (2, 1) != Square.EMPTY) and \
            (self.GetSquare (2, 2) != Square.EMPTY)

        return Draw

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

    def Turn(RandNumber):
        '''
        Creates the stating turn, and keeps track of the turn throughout the game

        Args:
            RandNumber (int): random number generated at the start and changed throughout to reflect the current turn.

        Returns:
            RandNumber (int): random number generated at the start and changed throughout to reflect the current turn.
            Letter (str (X or O)): The letter of who's turn it is
        '''

        Number = RandNumber % 2

        if Number == 1:
            Letter = Square.X

        elif Number == 0:
            Letter = Square.O

        RandNumber += 1

        print("It is's" ,Letter, " Turn\n ")

        return Letter, RandNumber

    def CheckSquare (board):
        '''
        Acts as the player turn
        Has input validation for the player turn to check if:
            the inputted value is only 2 characters long
            the square entered is empty 
        uses the functions LetterToCol/LetterToRow which changes the 2 letters to col/row format

        Args:
            board (object): The board of which the move will be made

        Returns:
            row (int): Vertical position of the board square (0 based).
            col (int): Horizontal position of the board square (0 based).
        '''

        print ("Input one of the following squares, Key: TL, TC, TR, ML, MC, MR, BL, BC, BR (e.g., TL = Top Left)")
         
        SquareCheck = False
        
        while SquareCheck == False:
            
            board.DisplayBoard()
            
            SquareInput = input("What square do you want to input? ").upper()
        
            if len(SquareInput) != 2:
                    print("\nInvalid input length. Please enter a 2-character code (e.g., TL, MC).")
                    continue

            col = Player.LetterToCol(SquareInput)
        
            row = Player.LetterToRow(SquareInput)
        
        
            SquareState = board.GetSquare(row, col)
            
            if SquareState != Square.EMPTY:
                print("\nSquare is not empty please re-enter")
        
            else:
                SquareCheck = True

        return row,col

    def Move(board, Letter, row ,col):
        '''
        Actually carries out the move made by the player/ computer

        Args:
            board (object): The board of which the move will be made
            Letter (str (X or O)): The letter of who's turn it is
            row (int): Vertical position of the board square (0 based).
            col (int): Horizontal position of the board square (0 based).
        '''

        board.SetSquare(row, col, Letter)
        board.DisplayBoard()


    def Computer(board):
        '''
        Acts as the Computer turn
        Does not have input validation for the turn as the computer only has set values to pick from
        (meaning there should be no outstanding values).
        uses the functions LetterToCol/LetterToRow which changes the 2 letters to col/row format
        
        Args:
            board (object): The board of which the move will be made

        Returns:
            row (int): Vertical position of the board square (0 based).
            col (int): Horizontal position of the board square (0 based).
        '''

        EmptySquare = False

        while EmptySquare == False:

            MovesDictionary = {0:"TL",1:"TC", 2:"TR", 3:"ML",4:"MC", 5:"MR", 6:"BL",7:"BC", 8:"BR"}

            DictionaryIndex = random.randint (0,8)

            RandomMove = MovesDictionary[DictionaryIndex]

            row = Player.LetterToRow(RandomMove)
            col = Player.LetterToCol(RandomMove)

            SquareState = board.GetSquare(row, col)

            if SquareState == Square.EMPTY:
                EmptySquare = True

        return row,col

    def LetterToRow(SquareInput):
        '''
        Changes the first letter to its corresponding row.
        Also if the letter doesn't match any it displays an error and asks the user to re-enter.

        Args:
            SquareInput (str): the inputted value from the user of the square they want to input.

        Return:
            row (int): Vertical position of the board square (0 based).
        '''

        if SquareInput[1] == "L":
            row = 0
                                    
        elif SquareInput[1] == "C":
            row = 1
                                    
        elif SquareInput[1] == "R":
            row = 2

        else:
            print("Invaded row, please start with T, M or B.")

        return row

    def LetterToCol(SquareInput):
        '''
        Changes the second letter to its corresponding col.
        Also if the letter doesn't match any it displays an error and asks the user to re-enter.
        
        Args:
            SquareInput (str): the inputted value from the user of the square they want to input.

        Return:
            col (int): horizontal position of the board square (0 based).
        '''

        if SquareInput[0] == "T":
            col = 0
                
        elif SquareInput[0] == "M":
            col = 1
                
        elif SquareInput[0] == "B":
            col = 2

        else:
            print("Invaded column, please end with L, C or R.")

        return col




def main():
    '''
    Run the board tests
    '''

    print("Tic tac toe game")

    board = Board()  # Create a new board

    RandNumber = random.randint(1,2)

    winX = board.GameWin(Square.X)
    winO = board.GameWin(Square.O)
    Draw = board.Draw()

    Index = 0

    GameMode = int(input("What game mode do you want to play if Player vs Player enter 1, if Player vs Computer enter 2, if Computer vs Computer (spectating) enter 3: "))

        
    def PlayPlayer():
        row,col = Player.CheckSquare(board)

        return row, col


    def PlayComputer():
        row,col = Player.Computer(board)

        return row, col


    def GameOver(winX, winO, Draw):

        winX = board.GameWin(Square.X)
        winO = board.GameWin(Square.O)
        Draw = board.Draw()

        if winX == True:
            print ("Player X has won")

        elif winO == True:
            print ("Player O has won")

        elif Draw == True:
            print ("The game is a draw")

        return winX, winO, Draw

    while winX == False and winO == False and Draw == False and Index <= 9:
        
        Letter, RandNumber = Player.Turn (RandNumber)

        if GameMode == 1:
            row, col = PlayPlayer()

        if GameMode == 2:
            row,col = PlayPlayer()

            Player.Move(board, Letter, row, col)

            winX, winO, Draw = GameOver(winX, winO, Draw)
                    
            Index += 1

            Letter, RandNumber = Player.Turn (RandNumber)

            row,col = PlayComputer()

        if GameMode == 3:
            row, col = PlayComputer()
        
        Player.Move(board, Letter, row, col)

        winX, winO, Draw = GameOver(winX, winO, Draw)
        
        Index += 1


# Entry point for the program, if run as a script
if __name__ == "__main__":
    main()