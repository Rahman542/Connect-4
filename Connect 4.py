#6x7 grid
#Numpy is used to spuuort multi dimensional array and data structures
#Had to go through my windows command prompt and install pip
#Once I had the updated version of pip I installed the updated version of numpy
#we use .zeros bebcause it will make a matrix of all 0's which is good for an intial state
#I had to research on data type objects
#I learned about f strings which are so concise, fast and easy to read, and usable on line 18
import numpy as np

#Decided to print a guidelines statement
print("""Hello all players, welcome to Connect 4.
In this game you will need two players. The point of the game simple.
Chose a row to drop your "chip"in. The first player able to connect four of
there chips together wins and gets Connect 4. This may be done vertically or horizontally
on the board. You can also place your chips to break connecting pieces to make sure your
opponent does not get Connect 4 first.

When playing this game be aware, that in order to drop your piece you have to pick the place
from 1-7 on where to drop it in the following row. 1 being to the most left and 7 to the most
right. Anything else will prompt that you input will reprompt you to input an integer from that
range.

Lastly, your "chips" are numbered. For player 1 there chips will say 1 on the board. For player
2 there chips will say 2 on the board.

Now have fun, and let's see who can get Connect 4 first""")

board=np.zeros((6,7), dtype=int)
   
#Need to make a list of allowed moves the player can make
allow= 7*[6]
move= 1
def player_turn():
    return 1 if move==1 else 2
#Made a function that will be used to change the turns
# These will indicate the chips as 1 will be player one and 2 will be 2

#function for valid moves, started with a while loop
def valid_move():
    while True:
        try:
            turn=int(input(f"What is player {player_turn()}'s move?, pick your row from (1-7) as a move "))-1
            if turn in range(7) and allow[turn] != 0:
                allow[turn]=allow[turn]-1
                return turn
            continue
        except ValueError:
            continue
   
### we add the -1 to change the indexing to 0
#Then we can check that the range is within 7 because there are only 7 colums after all
#We also need to make sure the move is VALID
# Now we need to subrtract the value from the variable for the accounting turn
#BUT we also need to account for values that are not integers or even STRINGS 
#A great and easy way is to use "try" for correct values and "except ValueError" for wrong values to continue to prompt the user in the while loop
#So essentially this function make sures the input is valid and is useful for the columns path

def four_square(row,column):
    for i in range(0 if row<=3 else row-3, 3 if row>=2 else row+1):
        for j in range(0 if column<=3 else column-3, 4 if column>=3 else column+1):
            position=board[i:i+4, j:j+4]
            for x in range(4):
                if sum(position[x])==move*4 or sum(position[:, x])==move*4:
                    return True
            if sum(np.diag(position))==move*4 or sum(np.diag(position[::-1]))==move*4:
                   return True

#need a function to check for 4 in a row 
#Learned the "idea" of i and j for loops, super useful for a case of dimensional construction
# For i used the idea of it being 6 rows
# For j used the idea of it being 7 rows
# the only difference between the for loops is you obvisouly want ot change the 3 to a 4 to account for the 7 columns rather than 6 rows
#.diag for a diagonal matrix, that returns the column vector 

def valid_row(value):
    return 5-np.where(board[::-1, value]==0)[0][0]

#Now we need to account for the row
# Similar to an x-y plane, we already calculated the x axis, the column, now we use that to find the row
#So in the second line of this function I needed to slice to flip the board bottom up
# I used numpy.where because the where function returns the indices of the elements in an input array
#When using numpy.where you need you need to absolutely have an index of 0
#But we want to flip it back so we subtract this from 5


def finished_board():
    print(np.where(board==-1, 2, board))

finished_board()
while True:
    turn=valid_move()
    row=valid_row(turn)
    board[row,turn]=move
    finished_board()
    if four_square(row, turn):
        print(f"Player{player_turn()} won the game, wayyyyyy to go champ!")
        break
    if sum(allow)==0:
        print("aww man the game ended in a draw, play again")
        break
    move*=-1
#arguement is turn which is our column


