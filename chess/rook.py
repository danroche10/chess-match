import pygame
from chess.helpers import Helpers
from chess.piece import Piece
from .constants import BLACK, WHITE

class Rook(Piece):
    def create(self, win, row, col):
        if self.get_color() == BLACK:
          win.blit(pygame.image.load('chess/assets/black_rook.png'), (col*100, row*100))
        else:
          win.blit(pygame.image.load('chess/assets/white_rook.png'), (col*100, row*100))

    def get_valid_rook_moves(self, board, row, col, color):
        moves = {}
        if color == BLACK:
            potential_move_col = col
            while potential_move_col <= 7:
              potential_move_col += 1
              if potential_move_col == 8:
                  break
              elif board[row][potential_move_col] == 0:
                  moves = Helpers.update_valid_moves(moves, row, potential_move_col)
              elif board[row][potential_move_col].get_color() == WHITE:
                  moves = Helpers.update_valid_moves(moves, row, potential_move_col)
                  moves[(row, potential_move_col)] = [board[row][potential_move_col]]
                  break
              elif board[row][col].get_color() == BLACK:
                  break
            potential_move_col = col

            while potential_move_col >= 0:
              potential_move_col -= 1
              if potential_move_col == -1:
                 break
              elif board[row][potential_move_col] == 0:
                  moves = Helpers.update_valid_moves(moves, row, potential_move_col)
              elif board[row][potential_move_col].get_color() == WHITE:
                  moves = Helpers.update_valid_moves(moves, row, potential_move_col)
                  moves[(row, potential_move_col)] = [board[row][potential_move_col]]
                  break
              elif board[row][potential_move_col].get_color() == BLACK:
                  break

            potential_move_row = row 
            while potential_move_row <= 7:
              potential_move_row += 1
              if potential_move_row == 8:
                  break
              elif board[potential_move_row][col] == 0:
                  moves = Helpers.update_valid_moves(moves, potential_move_row, col)
              elif board[potential_move_row][col].get_color() == WHITE:
                  moves = Helpers.update_valid_moves(moves, potential_move_row, col)
                  break
              elif board[row][col].get_color() == BLACK:
                  break
            potential_move_row = row 
            
            while potential_move_row >= 0:
              potential_move_row -= 1
              if potential_move_row == -1:
                 break
              elif board[potential_move_row][col] == 0:
                 moves = Helpers.update_valid_moves(moves, potential_move_row, col)
              elif board[potential_move_row][col].get_color() == WHITE:
                 moves = Helpers.update_valid_moves(moves, potential_move_row, col)
                 moves[(potential_move_row, col)] = [board[potential_move_row][col]]
                 break
              elif board[row][col].get_color() == BLACK:
                 break
            potential_move_row = row 
            
        return moves