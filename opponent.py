'''Module to program the computer opponent to play the game'''
import random

def transpose(grid):
    '''Function to return the transpose of a grid'''
    new_grid=[[0,0,0],[0,0,0],[0,0,0]]
    for row in range(3):
        for col in range(3):
            new_grid[col][row]=grid[row][col]
    return new_grid

# Function that will play the most optimal move for the opponent
def opponent_move(grid):     # Here, grid is the 2D list representing the actual grid
    '''

    The algorithm followed by the computer opponent goes like this:
    Step 1 : First, the opponent looks if there is any winning move or not.
             i.e. if there is any row, column or diagonal with two "O" and one "_" and then fills the "_" with "O".
    Step 2 : Now, if there is no winning move, the opponent looks if there is any player's winning move that can be blocked
             i.e. if there is any row, column or diagonal with two "X" and one "_" and then fills the "_" with "O".
    Step 3 : Now, the opponent looks for any row, column or diagonal of form ['O','_','_'] or ['_','_','O'] and if found, converts
             them to ['O','_','O'].
    Step 4 : If none of the above is possible, the opponent fills up any vacant corner square.
    Step 5 : If none of the above is possible, the opponent fills any random vacant square.

    '''

    # List of lists containing the diagonals of the grid
    diagonals=[
               [grid[0][0],grid[1][1],grid[2][2]],
               [grid[0][2],grid[1][1],grid[2][0]]
               ]

    # The opponent checks if there is a winning move
    # If there are two 'O' in a row, column or diagonal, the opponent will fill the blank space with a 'O'
    # If there are two 'O' in a row
    for row in range(len(grid)):
        if grid[row].count('O')==2 and grid[row].count('_')==1:
            grid[row]=['O','O','O']
            return grid
        
    # If there are two 'O' in a column
    new_grid=transpose(grid)
    for row in range(len(new_grid)):
        if new_grid[row].count('O')==2 and new_grid[row].count('_')==1:
            new_grid[row]=['O','O','O']
            grid=transpose(new_grid)
            return grid
        
    # If there are two 'O' in a diagonal
    for diagonal in range(len(diagonals)):
        if diagonals[diagonal].count('O')==2 and diagonals[diagonal].count('_')==1:
            diagonals[diagonal]=['O','O','O']
            if diagonal == 0:
                [grid[0][0],grid[1][1],grid[2][2]]=diagonals[diagonal]
            else:
                [grid[0][2],grid[1][1],grid[2][0]]=diagonals[diagonal]
            return grid
        
    # If there is no winning move, the opponent checks if the player has any winning move.
    # If there are two 'X' in a row, column or diagonal, the opponent will fill the blank space with a 'O'
    # If there are two 'X' in a row
    for row in range(len(grid)):
        if grid[row].count('X')==2 and grid[row].count('_')==1:
            grid[row]=list(map(lambda x:x.replace('_','O'),grid[row]))
            return grid
        
    # If there are two 'X' in a column
    new_grid=transpose(grid)
    for row in range(len(new_grid)):
        if new_grid[row].count('X')==2 and new_grid[row].count('_')==1:
            new_grid[row]=list(map(lambda x:x.replace('_','O'),new_grid[row]))
            grid=transpose(new_grid)
            return grid
        
    # If there are two 'X' in a diagonal
    for diagonal in range(len(diagonals)):
        if diagonals[diagonal].count('X')==2 and diagonals[diagonal].count('_')==1:
            diagonals[diagonal]=list(map(lambda x:x.replace('_','O'),diagonals[diagonal]))
            if diagonal == 0:
                [grid[0][0],grid[1][1],grid[2][2]]=diagonals[diagonal]
            else:
                [grid[0][2],grid[1][1],grid[2][0]]=diagonals[diagonal]
            return grid
    
    # If a row is of form ['O','_','_'] or ['_','_','O']
    for row in range(len(grid)):
        if grid[row]==['O','_','_'] or grid[row]==['_','_','O']:
            grid[row]=['O','_','O']
            return grid
        
    # If a column is of form ['O','_','_'] or ['_','_','O']
    new_grid=transpose(grid)
    for row in range(len(new_grid)):
        if new_grid[row]==['O','_','_'] or new_grid[row]==['_','_','O']:
            new_grid[row]=['O','_','O']
            grid=transpose(new_grid)
            return grid
        
    # If a diagonal is of form ['O','_','_'] or ['_','_','O']
    for diagonal in range(len(diagonals)):
        if diagonals[diagonal]==['O','_','_'] or diagonals[diagonal]==['_','_','O']:
            diagonals[diagonal]=['O','_','O']
            if diagonal == 0:
                [grid[0][0],grid[1][1],grid[2][2]]=diagonals[diagonal]
            else:
                [grid[0][2],grid[1][1],grid[2][0]]=diagonals[diagonal]
            return grid


    # If there are no winning moves for the player or opponent and threats can be made, the opponent fills up a vacant corner square
    if grid[0][0]=='_':
        grid[0][0]='O'
        return grid
    elif grid[0][2]=='_':
        grid[0][2]='O'
        return grid
    elif grid[2][0]=='_':
        grid[2][0]='O'
        return grid
    elif grid[2][2]=='_':
        grid[2][2]='O'
        return grid
    
    # If none of the above are possible, the opponent just fills up some random vacant square
    while True:
        r=random.randint(0,2)       # r denotes the row
        c=random.randint(0,2)       # c denotes the column
        if grid[r][c]=='_':
            grid[r][c]='O'
            return grid

