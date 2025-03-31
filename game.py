'''The main game file. Run this file to play the game.'''
# program where all the instructions are implemented and the driver code is written
# classes module is imported
import classes

# first the game is initialized
classes.Initiate.intro()

# input from player on who will go first
turn=classes.Initiate.turn()

# the grid is initialized
grid=classes.Initiate.initialize_grid()

# creating an instance of the class Game to store the grid
game_state=classes.Game(grid)

# displaying the grid at the beginning
print("\n")
game_state.display()
print("\n")


# the game will go on until the player wins or loses or the game is a draw
while  not(game_state.is_won() or game_state.is_draw()) :
    print("~"*10)
    if turn == -1:
        print("Computer's turn")
        grid=game_state.computer()
    elif turn == 1:
        print("Player's turn")
        grid=game_state.player()
    for row in grid:
        print(row)
    turn *= -1
    game_state=classes.Game(grid)

# what happens if the player wins or loses
if game_state.is_won():
    if turn == -1:
        classes.Ending.player_win()
    elif turn == 1:
        classes.Ending.player_lose()

# if the game is drawn
else:
    classes.Ending.game_drawn()