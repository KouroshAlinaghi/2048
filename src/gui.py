import random
import pygame
import math

from game import board
from main import size

window_inner_size = 600
window_margin = 10

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 36)
screen = pygame.display.set_mode((window_inner_size + window_margin, window_inner_size + window_margin + 100))

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

def draw_tile(num, x, y):
    draw_rect(pygame.Rect(x, y, window_inner_size / size, window_inner_size / size), get_color(num))
    draw_line((x, window_margin / 2), (x, y + window_inner_size / 4))
    offset = ((window_inner_size / size) - 36) / 2
    draw_text(num if num else " ", x + offset, y + offset)

def draw():
    global board
    x, y = window_margin / 2, window_margin / 2 + 100
    for row in board:
        x = window_margin / 2
        for square in row:
            draw_tile(square, x, y)
            x += window_inner_size / size
        draw_line((window_margin / 2, y), (window_inner_size + window_margin / 2, y))
        y += window_inner_size / size
