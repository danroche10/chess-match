import pygame
from .constants import SQUARE_SIZE, GREY

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color, type):
        self.row = row
        self.col = col
        self.color = color
        self.type = type
        self.x = 0
        self.y = 0
        self._calc_pos()
                 
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def type(self):
        return self.type

    def move(self, row, col):
        self.row = row
        self.col = col
        self._calc_pos()

    def _calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def __repr__(self):
        return str(self.color)
