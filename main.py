import pygame
import random
import math
import copy

board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
prev_board = copy.deepcopy(board)

window_inner_size = 600
window_margin = 10

random.seed()

pygame.init()
screen = pygame.display.set_mode((window_inner_size + window_margin, window_inner_size + window_margin + 100))
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 36)

score = 0
empties = 4 * 4

def sow_state():
    global board
    global empties

    for i in range(4):
        for j in range(4):
            if random.random() < 0.2:
                empties -= 1
                board[i][j] = (4 if random.random() > 7.0 else 2)

def get_color(num):
    if (num == 0):
        return (250, 250, 250)
    x = math.log2(num)
    r = 240;
    g = (-250/17)*x + 250;
    b = (25/8)*(x - 8)**2 + 50
    return (r, g, b)

def draw_text(text, x, y):
    text = str(text)
    font = pygame.font.Font(pygame.font.get_default_font(), 36)
    text = font.render(text, True, (0, 0, 0))
    screen.blit(text, (x, y))

def draw_line(s, d):
    pygame.draw.line(screen, "white", s, d)

def draw_rect(rect, color):
    pygame.draw.rect(screen, color, rect)

def draw():
    global board
    x, y = window_margin / 2, window_margin / 2 + 100
    for row in board:
        x = window_margin / 2
        for square in row:
            draw_rect(pygame.Rect(x, y, window_inner_size / 4, window_inner_size / 4), get_color(square))
            draw_line((x, window_margin / 2), (x, y + window_inner_size / 4))
            offset = ((window_inner_size / 4) - 36) / 2
            draw_text(square if square else " ", x + offset, y + offset)
            x += window_inner_size / 4
        draw_line((window_margin / 2, y), (window_inner_size + window_margin / 2, y))
        y += window_inner_size / 4

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
                elif board[k][j] != board[k-1][j]:
                    break

def seed():
    global board
    for i in range(4):
        for j in range(4):
            if not board[i][j] and random.random() < 0.1:
                board[i][j] = (4 if random.random() > 7.0 else 2)

def is_loser():
    global board
    for i in range(4):
        for j in range(3):
            if not board[i][j] or not board[i][j+1]:
                return False
            if board[i][j] == board[i][j+1]:
                return False

    for j in range(4):
        for i in range(3):
            if board[i][j] == board[i+1][j]:
                return False

    return True

def run():
    global prev_board
    global board

    sow_state()
    running = True

    while running:
        moved = False
        pushed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.__dict__["key"] == 1073741904:
                    prev_board = copy.deepcopy(board)
                    pushed = True;
                    move_left()
                elif event.__dict__["key"] == 1073741903:
                    prev_board = copy.deepcopy(board)
                    pushed = True;
                    move_right()
                elif event.__dict__["key"] == 1073741905:
                    prev_board = copy.deepcopy(board)
                    pushed = True;
                    move_down()
                elif event.__dict__["key"] == 1073741906:
                    prev_board = copy.deepcopy(board)
                    pushed = True;
                    move_up()

        if pushed:
            moved = prev_board != board

        if moved:
            seed()
            if is_loser():
                pygame.quit()

        screen.fill("white")
        draw_text("SCORE: {0}".format(score), 60, 40)
        draw()

        pygame.display.flip()

    pygame.quit()

run()
