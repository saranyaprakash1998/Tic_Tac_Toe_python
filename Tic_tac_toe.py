import random
board = [' ']*10
computer = 'X'
user = '0'


def display_board(board):
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('-' * 10)

def check_win():
    if board[1] == board[2] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] == board[9] and board[1] != ' ':
        return True
    elif board[3] == board[5] == board[7] and board[3] != ' ':
        return True
    else:
        return False

def check_draw():
    if board.count(' ') < 2:
        return True
    else:
        return False

def is_available(pos):
    return True if board[pos] == ' ' else False


def insert(letter, pos):
    if is_available(pos):
        board[pos] = letter
        display_board(board)
        if check_win():
            if letter == 'X':
                print("Computer Wins")
                exit()
            else:
                print("User Wins")
                exit()
        if check_draw():
            print("Draw")
            exit()
    else:
        if letter == '0':
            pos = int(input("Not free! Please re-enter a position"))
        else:
            pos = random.randint(1, 9)
        insert(letter, pos)


def user_move(letter):
    pos = int(input("Enter the position to be inserted:"))
    insert(letter, pos)

def computer_move(letter):
    pos = random.randint(1, 9)
    insert(letter, pos)

while not check_win():
    display_board(board)
    computer_move(computer)
    user_move(user)