import copy
import random

from main import LEFT, RIGHT, UP, DOWN, size

board = [[0 for j in range(size)] for i in range(size)]
prev_board = copy.deepcopy(board)

random.seed()

score = 0

def seed(tiles):
    global board
    tiles = int(tiles)
    for time in range(tiles):
        i, j = random.randint(0, 3), random.randint(0, 3)
        while board[i][j]:
            i, j = random.randint(0, 3), random.randint(0, 3)

        board[i][j] = (4 if random.random() > 9.0 else 2)

def is_loser():
    global board
    for i in range(size):
        for j in range(size-1):
            if not board[i][j] or not board[i][j+1]:
                return False
            if board[i][j] == board[i][j+1]:
                return False

    for j in range(size):
        for i in range(size-1):
            if board[i][j] == board[i+1][j]:
                return False

    return True

def move_right():
    global board
    global score
    for i in range(4):
        for j in reversed(range(0, 3)):
            if not board[i][j]:
                continue
            for k in range(j, 3):
                if board[i][k+1] == 0:
                    board[i][k], board[i][k+1] = board[i][k+1], board[i][k]
                elif board[i][k+1] == board[i][k]:
                    board[i][k+1] *= 2
                    score += board[i][k+1]
                    board[i][k] = 0
                    break
                elif board[i][k] != board[i][k+1]:
                    break

def move_left():
    global board
    global score
    for i in range(4):
        for j in range(1, 4):
            if not board[i][j]:
                continue
            for k in reversed(range(1, j + 1)):
                if board[i][k-1] == 0:
                    board[i][k], board[i][k-1] = board[i][k-1], board[i][k]
                elif board[i][k-1] == board[i][k]:
                    board[i][k-1] *= 2
                    score += board[i][k-1]
                    board[i][k] = 0
                    break
                elif board[i][k] != board[i][k-1]:
                    break

def move_down():
    global board
    global score
    for j in range(4):
        for i in reversed(range(0, 3)):
            if not board[i][j]:
                continue
            for k in range(i, 3):
                if board[k+1][j] == 0:
                    board[k][j], board[k+1][j] = board[k+1][j], board[k][j]
                elif board[k+1][j] == board[k][j]:
                    board[k+1][j] *= 2
                    score += board[k+1][j]
                    board[k][j] = 0
                    break
                elif board[k][j] != board[k+1][j]:
                    break

def move_up():
    global board
    global score
    for j in range(4):
        for i in range(1, 4):
            if not board[i][j]:
                continue
            for k in reversed(range(1, i + 1)):
                if board[k-1][j] == 0:
                    board[k][j], board[k-1][j] = board[k-1][j], board[k][j]
                elif board[k-1][j] == board[k][j]:
                    board[k-1][j] *= 2
                    score += board[k-1][j]
                    board[k][j] = 0
                    break
                elif board[k][j] != board[k-1][j]:
                    break

def move(d):
    if d == LEFT:
        move_left()
    elif d == RIGHT:
        move_right()
    elif d == UP:
        move_up()
    elif d == DOWN:
        move_down()
