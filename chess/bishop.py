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
    
    def get_valid_bishop_moves(self, board, current_row, current_col, color):
        moves = {}

        potential_move_current_col = current_col
        potential_move_current_row = current_row
        self._get_moves_to_right(moves, board, current_row, current_col, potential_move_current_row, potential_move_current_col, color)
        self._get_moves_to_left(moves, board, current_row, current_col, potential_move_current_row, potential_move_current_col, color)

        return moves

    def _get_moves_to_right(self, moves, board, current_row, current_col, potential_move_current_row, potential_move_current_col, color):
        self.get_moves_to_right_and_down(moves, board, current_row, current_col, potential_move_current_row, potential_move_current_col, color)
        self.get_moves_to_right_and_up(moves, board, current_row, current_col, potential_move_current_row, potential_move_current_col, color)

    def _get_moves_to_left(self, moves, board, current_row, current_col, potential_move_current_row, potential_move_current_col, color):
        self.get_moves_to_left_and_down(moves, board, current_row, current_col, potential_move_current_row, potential_move_current_col, color)
        self.get_moves_to_left_and_up(moves, board, current_row, current_col, potential_move_current_row, potential_move_current_col, color)

    def get_moves_to_right_and_down(self, moves, board, current_row, current_col, potential_move_current_row, potential_move_current_col, color):
        while potential_move_current_col <= 7 and potential_move_current_row <= 7:
          potential_move_current_col += 1
          potential_move_current_row += 1
          if potential_move_current_col == 8 or potential_move_current_row == 8:
              break
          elif board[potential_move_current_row][potential_move_current_col] == 0:
              moves = Helpers.update_valid_moves(moves, potential_move_current_row, potential_move_current_col)
          elif (board[potential_move_current_row][potential_move_current_col].get_color() == WHITE and color == BLACK) or (board[potential_move_current_row][potential_move_current_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, potential_move_current_row, potential_move_current_col)
              moves[(potential_move_current_row, potential_move_current_col)] = [board[potential_move_current_row][potential_move_current_col]]
              break
          elif (board[potential_move_current_row][potential_move_current_col].get_color() == BLACK and color == BLACK) or (board[potential_move_current_row][potential_move_current_col].get_color() == WHITE and color == WHITE):
              break
        potential_move_current_col = current_col
        potential_move_current_row = current_row
    
    def get_moves_to_right_and_up(self, moves, board, current_row, current_col, potential_move_current_row, potential_move_current_col, color):
        while potential_move_current_col <= 7 and potential_move_current_row >= 0:
          potential_move_current_col += 1
          potential_move_current_row -= 1
          if potential_move_current_col == 8 or potential_move_current_row == -1:
              break
          elif board[potential_move_current_row][potential_move_current_col] == 0:
              moves = Helpers.update_valid_moves(moves, potential_move_current_row, potential_move_current_col)
          elif (board[potential_move_current_row][potential_move_current_col].get_color() == WHITE and color == BLACK) or (board[potential_move_current_row][potential_move_current_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, potential_move_current_row, potential_move_current_col)
              moves[(potential_move_current_row, potential_move_current_col)] = [board[potential_move_current_row][potential_move_current_col]]
              break
          elif (board[potential_move_current_row][potential_move_current_col].get_color() == BLACK and color == BLACK) or (board[potential_move_current_row][potential_move_current_col].get_color() == WHITE and color == WHITE):
              break
        potential_move_current_col = current_col
        potential_move_current_row = current_row
    
    def get_moves_to_left_and_down(self, moves, board, current_row, current_col, potential_move_current_row, potential_move_current_col, color):
        while potential_move_current_col >= 0 and potential_move_current_row >= 0:
          potential_move_current_col -= 1
          potential_move_current_row -= 1
          if potential_move_current_col == -1 or potential_move_current_row == -1:
              break
          elif board[potential_move_current_row][potential_move_current_col] == 0:
              moves = Helpers.update_valid_moves(moves, potential_move_current_row, potential_move_current_col)
          elif (board[potential_move_current_row][potential_move_current_col].get_color() == WHITE and color == BLACK) or (board[potential_move_current_row][potential_move_current_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, potential_move_current_row, potential_move_current_col)
              moves[(potential_move_current_row, potential_move_current_col)] = [board[potential_move_current_row][potential_move_current_col]]
              break
          elif (board[potential_move_current_row][potential_move_current_col].get_color() == BLACK and color == BLACK) or (board[potential_move_current_row][potential_move_current_col].get_color() == WHITE and color == WHITE):
              break
        potential_move_current_col = current_col
        potential_move_current_row = current_row

    def get_moves_to_left_and_up(self, moves, board, current_row, current_col, potential_move_current_row, potential_move_current_col, color):
        while potential_move_current_col >= 0 and potential_move_current_row <= 7:
          potential_move_current_col -= 1
          potential_move_current_row += 1
          if potential_move_current_col == -1 or potential_move_current_row == 8:
              break
          elif board[potential_move_current_row][potential_move_current_col] == 0:
              moves = Helpers.update_valid_moves(moves, potential_move_current_row, potential_move_current_col)
          elif (board[potential_move_current_row][potential_move_current_col].get_color() == WHITE and color == BLACK) or (board[potential_move_current_row][potential_move_current_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, potential_move_current_row, potential_move_current_col)
              break
          elif (board[potential_move_current_row][potential_move_current_col].get_color() == BLACK and color == BLACK) or (board[potential_move_current_row][potential_move_current_col].get_color() == WHITE and color == WHITE):
              break
        potential_move_current_col = current_col
        potential_move_current_row = current_row



        



        
