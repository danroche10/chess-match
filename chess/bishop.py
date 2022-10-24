import pygame
from chess.helpers import Helpers
from chess.piece import Piece
from .constants import BLACK, WHITE

class Bishop(Piece):
    def create(self, win, row, col):
        if self.get_color() == BLACK:
          win.blit(pygame.image.load('chess/assets/black_bishop.png'), (col*100, row*100))
        else:
          win.blit(pygame.image.load('chess/assets/white_bishop.png'), (col*100, row*100))
    
    def get_valid_bishop_moves(self, board, row, col, color):
        moves = {}

        potential_move_col = col
        potential_move_row = row
        while potential_move_col <= 7 and potential_move_row <= 7:
          potential_move_col += 1
          potential_move_row += 1
          if potential_move_col == 8 or potential_move_row == 8:
              break
          elif board[potential_move_row][potential_move_col] == 0:
              moves = Helpers.update_valid_moves(moves, potential_move_row, potential_move_col)
          elif (board[potential_move_row][potential_move_col].get_color() == WHITE and color == BLACK) or (board[potential_move_row][potential_move_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, potential_move_row, potential_move_col)
              moves[(potential_move_row, potential_move_col)] = [board[potential_move_row][potential_move_col]]
              break
          elif (board[potential_move_row][potential_move_col].get_color() == BLACK and color == BLACK) or (board[potential_move_row][potential_move_col].get_color() == WHITE and color == WHITE):
              break
        potential_move_col = col
        potential_move_row = row

        while potential_move_col >= 0 and potential_move_row >= 0:
          potential_move_col -= 1
          potential_move_row -= 1
          if potential_move_col == -1 or potential_move_row == -1:
              break
          elif board[potential_move_row][potential_move_col] == 0:
              moves = Helpers.update_valid_moves(moves, potential_move_row, potential_move_col)
          elif (board[potential_move_row][potential_move_col].get_color() == WHITE and color == BLACK) or (board[potential_move_row][potential_move_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, potential_move_row, potential_move_col)
              moves[(potential_move_row, potential_move_col)] = [board[potential_move_row][potential_move_col]]
              break
          elif (board[row][potential_move_col].get_color() == BLACK and color == BLACK) or (board[row][potential_move_col].get_color() == WHITE and color == WHITE):
              break
        potential_move_col = col
        potential_move_row = row

        while potential_move_col >= 0 and potential_move_row <= 7:
          potential_move_col -= 1
          potential_move_row += 1
          if potential_move_col == -1 or potential_move_row == 8:
              break
          elif board[potential_move_row][potential_move_col] == 0:
              moves = Helpers.update_valid_moves(moves, potential_move_row, potential_move_col)
          elif (board[potential_move_row][potential_move_col].get_color() == WHITE and color == BLACK) or (board[potential_move_row][potential_move_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, potential_move_row, potential_move_col)
              break
          elif (board[potential_move_row][potential_move_col].get_color() == BLACK and color == BLACK) or (board[potential_move_row][potential_move_col].get_color() == WHITE and color == WHITE):
              break
        potential_move_col = col
        potential_move_row = row
        
        while potential_move_col <= 7 and potential_move_row >= 0:
          potential_move_col += 1
          potential_move_row -= 1
          if potential_move_col == 8 or potential_move_row == -1:
              break
          elif board[potential_move_row][potential_move_col] == 0:
              moves = Helpers.update_valid_moves(moves, potential_move_row, potential_move_col)
          elif (board[potential_move_row][potential_move_col].get_color() == WHITE and color == BLACK) or (board[potential_move_row][potential_move_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, potential_move_row, potential_move_col)
              moves[(potential_move_row, potential_move_col)] = [board[potential_move_row][potential_move_col]]
              break
          elif (board[potential_move_row][potential_move_col].get_color() == BLACK and color == BLACK) or (board[potential_move_row][potential_move_col].get_color() == WHITE and color == WHITE):
              break
        potential_move_col = col
        potential_move_row = row
        
        return moves
