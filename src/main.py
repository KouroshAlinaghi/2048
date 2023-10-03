import pygame
import sys

from game import Game
from gui import GUI

pygame.init()

def main():
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    game = Game(size)
    gui = GUI(size)

    game.start(gui)

if __name__ == "__main__":
    main()
