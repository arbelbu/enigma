import random
from operator import itemgetter
x="X"
o="O"

board=list(" "*9)


lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
rows = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
diagonals = [[0, 4, 8], [2, 4, 6]]
wins = (lines + rows + diagonals)

def print_board(board):

    for i in range(0,3):
        print("|".join(board[i*3:(i+1)*3]))
        print("-+-+-")

def number_to_xo_(board):
    return dict(zip(range(0,9),board))





def first_queue (board):
    if board[4] == x:
        return random.choice([0, 2, 6, 8])
    else:
        return 4

def fork ():
    for line in lines:
        for row_or_diagonal in (rows + diagonals):
            if number_to_xo_(board)[next(iter(set(line).intersection(set(row_or_diagonal))))] == {" "} and line.count(o) == 1 and row_or_diagonal.count(o) == 1 and line.count(" ") == 2 and row_or_diagonal.count(" ") == 2:
                return next(iter(set(line).intersection(set(row_or_diagonal))))
    for row in rows:
        for diagonal in (diagonals):
            if number_to_xo_(board)[next(iter(set(row).intersection(set(diagonal))))] == " " and row.count(o) == 1 and diagonal.count(o) == 1 and row.count(" ") == 2 and diagonal.count(" ") == 2:
                return next(iter(set(row).intersection(set(diagonal))))
    return None

def win_or_block(board):
    for win in wins:
        win_xo = "".join([number_to_xo_(board)[a] for a in win])
        if   win_xo.count(o) == 2 and win_xo.count(" ") == 1:
            return win[win_xo.index(" ")]
        elif win_xo.count(x) == 2 and win_xo.count(" ") == 1:
            return win[win_xo.index(" ")]
    return None
assert win_or_block(['O', 'O', ' ', 'X', 'X', ' ', ' ', 'X', ' ']) == 2
assert win_or_block(['O', 'X', ' ', ' ', 'X', ' ', ' ', ' ', ' ']) == 7






def computer_player (board):
    list_of_empty_corner = [a for a in itemgetter(0, 2, 6, 8)(board) if a == " "]
    for win in wins:
        if win_or_block(board) != None:
            return win_or_block(board)
        elif fork () !=None:
            return fork ()

        elif (board[0] == x and board[8] == x) or (board[2] == x and board[6] == x):
            return random.choice([1, 3, 5, 7])



        elif (board[3] == x and board[1] == x):
            if board[8] == o:
                return random.choice([6, 2])
            else:
                return 4
        elif (board[1] == x and board[5] == x):
            if board[6] == o:
                return random.choice([0, 8])
            else:
                return 4
        elif (board[7] == x and board[5] == x):
            if board[0] == o:
                return random.choice([2, 6])
            else:
                return 4
        elif (board[3] == x and board[7] == x):
            if board[7] == o:
                return random.choice([0, 8])
            else:
                return 4


        elif list_of_empty_corner != []:
            return random.choice(list_of_empty_corner)
        else:
            return random.choice([i for i,b in enumerate(board) if b == " "])











def who_win(board):
    for win in wins:
        if board[int(win[0])]==board[int(win[1])]==board[int(win[2])]=='O':
            return ("o")
        elif board[int(win[0])]==board[int(win[1])]==board[int(win[2])]=='X':
            return ("x")


def main (board):

    first_x = int(input(""))
    board[first_x] = x
    board[first_queue(board)] = o
    print_board(board)

    seccond_x = int(input(""))
    board[seccond_x] = x
    board[computer_player(board)] = o
    print_board(board)

    third_x = int(input(""))
    board[third_x] = x
    board[computer_player(board)] = o
    print_board(board)
    if who_win(board) == "o":
        print("the O has won!")
    elif who_win(board) == "x":
        print("the X has won!")
    else:
        print("None")

    fourth_x = int(input(""))
    board[fourth_x] = x
    board[computer_player(board)] = o
    print_board(board)
    if who_win(board) == "o":
        print("the O has won!")
    elif who_win(board) == "x":
        print("the X has won!")
    else:
        print("None")

    fifth_x = int(input(""))
    board[fifth_x] = x
    print_board(board)
    if who_win(board) == "x":
        print( "the X has won!")
    else:
        print("tie")

#board = ['X', ' ', ' ', 'O', 'O', 'X', ' ', 'O', 'X']
#win_or_block(board)
main(board)

"""
sum_numbers=""
#for two players (not computer)
while True:
    a = int(input(""))
    sum_numbers+=str(a)
    if (len(sum_numbers)+1)%2==0:
        board[a]=x
    else:
        board[a] = o
    print(who_win(board))
    print_board(board)
"""







