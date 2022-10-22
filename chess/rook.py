import pygame
from chess.helpers import Helpers
from chess.piece import Piece
from .constants import BLACK

class Rook(Piece):
    def create(self, win, row, col):
        if self.get_color() == BLACK:
          win.blit(pygame.image.load('chess/assets/black_rook.png'), (col*100, row*100))
        else:
          win.blit(pygame.image.load('chess/assets/white_rook.png'), (col*100, row*100))

    def get_valid_pawn_moves(self, board, row, col, color):
      return "test"
