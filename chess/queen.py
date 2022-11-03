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
        potential_move_row = current_row
        potential_move_col = current_col
        self._get_moves_to_right_horizontal(moves, board, current_row, current_col, potential_move_col, color)
        self._get_moves_to_left_horizontal(moves, board, current_row, potential_move_col, color)
        self._get_moves_vertical_down(moves, board, current_row, current_col, potential_move_row, color)
        self._get_moves_vertical_up(moves, board, current_row, current_col, potential_move_row, color)
        self._get_moves_right_diagonal_down(moves, board, current_row, current_col, potential_move_row, potential_move_col, color)
        self._get_moves_right_diagonal_up(moves, board, current_row, current_col, potential_move_row, potential_move_col, color)
        self._get_moves_left_diagonal_up(moves, board, current_row, current_col, potential_move_row, potential_move_col, color)
        self._get_moves_right_diagonal_up(moves, board, current_row, current_col, potential_move_row, potential_move_col, color)
            
        return moves
    
    def _get_moves_to_right_horizontal(self, moves, board, current_row, current_col, potential_move_col, color):
        while potential_move_col <= 7:
            potential_move_col += 1
            if potential_move_col == 8:
                break
            elif board[current_row][potential_move_col] == 0:
                moves = Helpers.update_valid_moves(moves, current_row, potential_move_col)
            elif (board[current_row][potential_move_col].get_color() == WHITE and color == BLACK) or (board[current_row][potential_move_col].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row, potential_move_col)
                moves[(current_row, potential_move_col)] = [board[current_row][potential_move_col]]
                break
            elif (board[current_row][current_col].get_color() == BLACK and color == BLACK) or (board[current_row][current_col].get_color() == WHITE and color == WHITE):
                break
        potential_move_col = current_col

    def _get_moves_to_left_horizontal(self, moves, board, current_row, potential_move_col, color):
        while potential_move_col >= 0:
          potential_move_col -= 1
          if potential_move_col == -1:
              break
          elif board[current_row][potential_move_col] == 0:
              moves = Helpers.update_valid_moves(moves, current_row, potential_move_col)
          elif (board[current_row][potential_move_col].get_color() == WHITE and color == BLACK) or (board[current_row][potential_move_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, current_row, potential_move_col)
              moves[(current_row, potential_move_col)] = [board[current_row][potential_move_col]]
              break
          elif (board[current_row][potential_move_col].get_color() == BLACK and color == BLACK) or (board[current_row][potential_move_col].get_color() == WHITE and color == WHITE):
              break
        
        potential_move_col = current_row 

    def _get_moves_vertical_up(self, moves, board, current_row, current_col, potential_move_row, color):
        while potential_move_row >= 0:
          potential_move_row -= 1
          if potential_move_row == -1:
              break
          elif board[potential_move_row][current_col] == 0:
              moves = Helpers.update_valid_moves(moves, potential_move_row, current_col)
          elif (board[potential_move_row][current_col].get_color() == WHITE and color == BLACK) or (board[potential_move_row][current_col].get_color() == BLACK and color == WHITE):
              moves = Helpers.update_valid_moves(moves, potential_move_row, current_col)
              moves[(potential_move_row, current_col)] = [board[potential_move_row][current_col]]
              break
          elif (board[current_row][current_col].get_color() == BLACK and color == BLACK) or (board[current_row][current_col].get_color() == WHITE and color == WHITE):
              break
        
        potential_move_row = current_row
        
    def _get_moves_vertical_down(self, moves, board, current_row, current_col, potential_move_row, color):
        while potential_move_row <= 7:
            potential_move_row += 1
            if potential_move_row == 8:
                break
            elif board[potential_move_row][current_col] == 0:
                moves = Helpers.update_valid_moves(moves, potential_move_row, current_col)
            elif (board[potential_move_row][current_col].get_color() == WHITE and color == BLACK) or (board[potential_move_row][current_col].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, potential_move_row, current_col)
                break
            elif (board[current_row][current_col].get_color() == BLACK and color == BLACK) or (board[current_row][current_col].get_color() == WHITE and color == WHITE):
                break
        
        potential_move_row = current_row 
    
    def _get_moves_right_diagonal_up(self, moves, board, current_row, current_col, potential_move_row, potential_move_col, color):
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
        
        potential_move_row = current_row
        potential_move_col = current_col
    
    def _get_moves_right_diagonal_down(self, moves, board, current_row, current_col, potential_move_row, potential_move_col, color):
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
        
        potential_move_row = current_row
        potential_move_col = current_col
    
    def _get_moves_left_diagonal_up(self, moves, board, current_row, current_col, potential_move_row, potential_move_col, color):
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
            elif (board[potential_move_row][potential_move_col].get_color() == BLACK and color == BLACK) or (board[potential_move_row][potential_move_col].get_color() == WHITE and color == WHITE):
                break
        
        potential_move_row = current_row
        potential_move_col = current_col
    
    def _get_moves_left_diagonal_down(self, moves, board, current_row, current_col, potential_move_row, potential_move_col, color):
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
        
        potential_move_row = current_row
        potential_move_col = current_col
        
