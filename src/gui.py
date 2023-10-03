import random
import pygame
import math

class GUI:
    def __init__(self, size):
        self.window_inner_size = 600
        self.window_margin = 10
        self.font_size = int((self.window_inner_size / size) / 6)
        self.screen = pygame.display.set_mode((self.window_inner_size + self.window_margin, self.window_inner_size + self.window_margin + 100))

    def draw_text(self, text, x, y, text_size):
        text = str(text)
        font = pygame.font.Font(pygame.font.get_default_font(), text_size)
        text = font.render(text, True, (0, 0, 0))
        self.screen.blit(text, (x, y))

    def draw_line(self, s, d):
        pygame.draw.line(self.screen, "white", s, d)

    def draw_rect(self, rect, color):
        pygame.draw.rect(self.screen, color, rect)

    def draw_tile(self, num, x, y, size):
        self.draw_rect(pygame.Rect(x, y, self.window_inner_size / size, self.window_inner_size / size), get_color(num))
        self.draw_line((x, self.window_margin / 2), (x, y + self.window_inner_size / 4))
        offset = ((self.window_inner_size / size) - self.font_size) / 2
        self.draw_text(num if num else " ", x + offset, y + offset, self.font_size)

    def draw_board(self, board):
        size = len(board)
        x, y = self.window_margin / 2, self.window_margin / 2 + 100
        for row in board:
            x = self.window_margin / 2
            for square in row:
                self.draw_tile(square, x, y, size)
                x += self.window_inner_size / size
            self.draw_line((self.window_margin / 2, y), (self.window_inner_size + self.window_margin / 2, y))
            y += self.window_inner_size / size

    def refresh_and_draw(self, board, score):
        self.screen.fill("white")
        self.draw_text("SCORE: {0}".format(score), 60, 40, 36)
        self.draw_board(board)
        pygame.display.flip()


def get_color(num):
    if (num == 0):
        return (250, 250, 250)
    x = math.log2(num)
    r = 240;
    g = (-250/17)*x + 250;
    b = (25/8)*(x - 8)**2 + 50
    return (r, g, b)
