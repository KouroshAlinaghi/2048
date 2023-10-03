import copy
import pygame
import random

RIGHT, UP, LEFT, DOWN = range(4)
keys_map = {
    1073741904: LEFT,
    1073741903: RIGHT,
    1073741906: UP,
    1073741905: DOWN,
}

class Game:
    def __init__(self, size = 4):
        random.seed()

        self.board = [[0 for j in range(size)] for i in range(size)]
        self.prev_board = copy.deepcopy(self.board)
        self.score = 0
        self.size = size
        self.running = True

    def seed(self, num_of_tiles):
        num_of_tiles = int(num_of_tiles)
        for t in range(num_of_tiles):
            i, j = random.randint(0, self.size-1), random.randint(0, self.size-1)
            while self.board[i][j]:
                i, j = random.randint(0, self.size-1), random.randint(0, self.size-1)

            self.board[i][j] = (4 if random.random() > 9.0 else 2)

    def is_loser(self):
        for i in range(self.size):
            for j in range(self.size-1):
                if not self.board[i][j] or not self.board[i][j+1]:
                    return False
                if self.board[i][j] == self.board[i][j+1]:
                    return False

        for j in range(self.size):
            for i in range(self.size-1):
                if self.board[i][j] == self.board[i+1][j]:
                    return False

        return True

    def move_right(self):
        for i in range(self.size):
            for j in reversed(range(0, self.size-1)):
                if not self.board[i][j]:
                    continue
                for k in range(j, self.size-1):
                    if self.board[i][k+1] == 0:
                        self.board[i][k], self.board[i][k+1] = self.board[i][k+1], self.board[i][k]
                    elif self.board[i][k+1] == self.board[i][k]:
                        self.board[i][k+1] *= 2
                        self.score += self.board[i][k+1]
                        self.board[i][k] = 0
                        break
                    elif self.board[i][k] != self.board[i][k+1]:
                        break

    def move_left(self):
        for i in range(self.size):
            for j in range(1, self.size):
                if not self.board[i][j]:
                    continue
                for k in reversed(range(1, j + 1)):
                    if self.board[i][k-1] == 0:
                        self.board[i][k], self.board[i][k-1] = self.board[i][k-1], self.board[i][k]
                    elif self.board[i][k-1] == self.board[i][k]:
                        self.board[i][k-1] *= 2
                        self.score += self.board[i][k-1]
                        self.board[i][k] = 0
                        break
                    elif self.board[i][k] != self.board[i][k-1]:
                        break

    def move_down(self):
        for j in range(self.size):
            for i in reversed(range(0, self.size-1)):
                if not self.board[i][j]:
                    continue
                for k in range(i, self.size-1):
                    if self.board[k+1][j] == 0:
                        self.board[k][j], self.board[k+1][j] = self.board[k+1][j], self.board[k][j]
                    elif self.board[k+1][j] == self.board[k][j]:
                        self.board[k+1][j] *= 2
                        self.score += self.board[k+1][j]
                        self.board[k][j] = 0
                        break
                    elif self.board[k][j] != self.board[k+1][j]:
                        break

    def move_up(self):
        for j in range(self.size):
            for i in range(1, self.size):
                if not self.board[i][j]:
                    continue
                for k in reversed(range(1, i + 1)):
                    if self.board[k-1][j] == 0:
                        self.board[k][j], self.board[k-1][j] = self.board[k-1][j], self.board[k][j]
                    elif self.board[k-1][j] == self.board[k][j]:
                        self.board[k-1][j] *= 2
                        self.score += self.board[k-1][j]
                        self.board[k][j] = 0
                        break
                    elif self.board[k][j] != self.board[k-1][j]:
                        break

    def move(self, d):
        if d == LEFT:
            self.move_left()
        elif d == RIGHT:
            self.move_right()
        elif d == UP:
            self.move_up()
        elif d == DOWN:
            self.move_down()

    def start(self, gui):
        self.seed(max(self.size/2, 2))

        while self.running:
            moved = False
            pushed = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.__dict__["key"] in keys_map:
                        self.prev_board = copy.deepcopy(self.board)
                        pushed = True;
                        self.move(keys_map[event.__dict__["key"]])

            if pushed:
                moved = self.prev_board != self.board

            if moved:
                if self.is_loser():
                    print("You are a loser.")
                    pygame.quit()
                self.seed(max(1, self.size/4))

            gui.refresh_and_draw(self.board, self.score)

        pygame.quit()

