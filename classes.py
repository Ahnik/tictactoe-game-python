'''Module containing all the relevant classes and functions for the program'''

import opponent
# the superclass containing all other classes
class TicTacToe(object):
    '''The superclass containing all other classes required in the program'''
    pass

class Initiate(TicTacToe):
    '''Class containing all the instructions to be executed before the game starts'''

    @staticmethod
    def intro():
        '''Function to display the introduction at the starting of every game'''
        print("~"*30)
        print("Welcome to a game of TicTacToe.")
        print("X = Player")
        print("O = Computer")
        print("Good luck!")

    @staticmethod
    def turn():
        '''Function to take input from the user on whether they will start the game or the computer will start the game'''
        turn=int(input("Would you like to go first or second? Answer using 1 or 2 : "))

        # the turn variable is taken as 1 or -1 as then it will be easier to switch turns
        # you just multiply turn by -1
        if turn == 2:
            turn=-1
        return turn

    @staticmethod
    def initialize_grid():
        '''Function to initialize the grid on which the game will be played'''
        grid=[]
        for row in range(3):
            grid.append(["_","_","_"])
        return grid
    
class Game(TicTacToe):
    '''Class containing all the instructions to be executed during each turn in the game'''

    # the constructor
    def __init__(self,grid):
        '''An instance of this class will contain the game state which will be just the grid state'''
        self.grid=grid

    def player(self):
        '''This method is called when it's the player's turn to move'''  
        grid=self.grid
        row=int(input("Enter the row :")) 
        col=int(input("Enter the column :"))
        grid[row-1][col-1]="X"
        return grid
    
    def computer(self):
        '''This method is called when it's the computer's turn to move'''
        grid=self.grid
        grid=opponent.opponent_move(grid)
        return grid
    
    def is_won(self):
        '''To check the game state and determine if the game is won by someone or not. 
        Returns True if the game is won, otherwise returns False'''
        # if False the game is not won, if True the game is won
        grid=self.grid
        won=False

        # if a row contains all 'X' or all 'O' , the game is won
        for row in range(3):
            won=(grid[row]==["O","O","O"] or grid[row]==["X","X","X"]) or won
            if won == True:
                break
        
        # if a column contains all 'X' or all 'O', the game is won
        for col in range(3):
            if won == True:
                break
            won=(grid[0][col]==grid[1][col]==grid[2][col]!="_") or won

        # if a diagonal contains all 'X' or all 'O', the game is won
        if won == False:
            won=(grid[0][0]==grid[1][1]==grid[2][2]!="_") or won

        if won == False:
            won=(grid[0][2]==grid[1][1]==grid[2][0]!="_") or won
        
        return won
    
    def is_draw(self):
        '''To check the game state and determine if the game is a draw or not.
        Returns True if the game is a draw. Returns False otherwise.
        This method is to be only called if game.is_won()==False'''

        grid=self.grid

        # counts the number of rows with vacant spaces left
        count=0

        # if the entire grid is filled up and the game is not won, the game is a draw
        for row in grid:
            count += row.count("_")
        
        return (count == 0)
    
    def display(self):
        '''Method to display the current game state i.e. the grid'''
        grid=self.grid
        for row in grid:
            print(row)


class Ending(TicTacToe):
    '''Class containing all the instructions to be executed for the game to end'''

    @staticmethod
    def player_win():
        '''Instructions to be executed if the player wins'''
        print("Congratulations! You won!")

    @staticmethod
    def player_lose():
        '''Instructions to be executed if the player loses'''
        print("You lost. Better luck next time.")
    
    @staticmethod
    def game_drawn():
        '''Instructions to be executed if the game is drawn'''
        print("The game is drawn.")