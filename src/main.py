import pygame
import copy

from gui import *
from game import *
import game

RIGHT, UP, LEFT, DOWN = range(4)
keys_map = {
    1073741904: LEFT,
    1073741903: RIGHT,
    1073741906: UP,
    1073741905: DOWN,
}

def main():
    global prev_board
    global board

    seed(2)
    running = True

    while running:
        moved = False
        pushed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.__dict__["key"] in keys_map:
                    prev_board = copy.deepcopy(board)
                    pushed = True;
                    move(keys_map[event.__dict__["key"]])

        if pushed:
            moved = prev_board != board

        if moved:
            seed(1)
            if is_loser():
                print("You are a loser.")
                pygame.quit()

        screen.fill("white")
        draw_text("SCORE: {0}".format(game.score), 60, 40)
        draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
