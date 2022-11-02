import pygame
from chess.helpers import Helpers
from chess.piece import Piece
from .constants import BLACK, WHITE

class Queen(Piece):
    def create(self, win, row, col):
        if self.get_color() == BLACK:
          win.blit(pygame.image.load('chess/assets/black_queen.png'), (col*100, row*100))
        else:
          win.blit(pygame.image.load('chess/assets/white_queen.png'), (col*100, row*100))

    def get_valid_queen_moves(self, board, current_row, current_col, color):
        moves = {}
        potential_move_current_col = current_col
        while potential_move_current_col <= 7:
          potential_move_current_col += 1
          if potential_move_current_col == 8:
              break
          elif board[current_row][potential_move_current_col] == 0:
              moves = Helpers.update_valid_moves(moves, current_row, potential_move_current_col)
          elif (board[current_row][potential_move_current_col].get_color() == WHITE and color == BLACK) or (board[current_row][potential_move_current_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, current_row, potential_move_current_col)
              moves[(current_row, potential_move_current_col)] = [board[current_row][potential_move_current_col]]
              break
          elif (board[current_row][current_col].get_color() == BLACK and color == BLACK) or (board[current_row][current_col].get_color() == WHITE and color == WHITE):
              break
        potential_move_current_col = current_col

        while potential_move_current_col >= 0:
          potential_move_current_col -= 1
          if potential_move_current_col == -1:
              break
          elif board[current_row][potential_move_current_col] == 0:
              moves = Helpers.update_valid_moves(moves, current_row, potential_move_current_col)
          elif (board[current_row][potential_move_current_col].get_color() == WHITE and color == BLACK) or (board[current_row][potential_move_current_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, current_row, potential_move_current_col)
              moves[(current_row, potential_move_current_col)] = [board[current_row][potential_move_current_col]]
              break
          elif (board[current_row][potential_move_current_col].get_color() == BLACK and color == BLACK) or (board[current_row][potential_move_current_col].get_color() == WHITE and color == WHITE):
              break

        potential_move_current_row = current_row 
        while potential_move_current_row <= 7:
          potential_move_current_row += 1
          if potential_move_current_row == 8:
              break
          elif board[potential_move_current_row][current_col] == 0:
              moves = Helpers.update_valid_moves(moves, potential_move_current_row, current_col)
          elif (board[potential_move_current_row][current_col].get_color() == WHITE and color == BLACK) or (board[potential_move_current_row][current_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, potential_move_current_row, current_col)
              break
          elif (board[current_row][current_col].get_color() == BLACK and color == BLACK) or (board[current_row][current_col].get_color() == WHITE and color == WHITE):
              break
        potential_move_current_row = current_row 
        
        while potential_move_current_row >= 0:
          potential_move_current_row -= 1
          if potential_move_current_row == -1:
              break
          elif board[potential_move_current_row][current_col] == 0:
              moves = Helpers.update_valid_moves(moves, potential_move_current_row, current_col)
          elif (board[potential_move_current_row][current_col].get_color() == WHITE and color == BLACK) or (board[potential_move_current_row][current_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, potential_move_current_row, current_col)
              moves[(potential_move_current_row, current_col)] = [board[potential_move_current_row][current_col]]
              break
          elif (board[current_row][current_col].get_color() == BLACK and color == BLACK) or (board[current_row][current_col].get_color() == WHITE and color == WHITE):
              break
        potential_move_current_row = current_row

        potential_move_current_col = current_col
        potential_move_current_row = current_row
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
            
        return moves
