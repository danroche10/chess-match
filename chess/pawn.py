import pygame
from chess.helpers import Helpers
from chess.piece import Piece
from .constants import BLACK, WHITE

class Pawn(Piece):
    def create(self, win, row, col):
        if self.get_color() == BLACK:
          win.blit(pygame.image.load('chess/assets/black_pawn.png'), (col*100, row*100))
        else:
          win.blit(pygame.image.load('chess/assets/white_pawn.png'), (col*100, row*100))

    def get_valid_pawn_moves(self, board, current_row, current_col, color):
      moves = {}
      if color == BLACK:
        if Pawn._one_square_ahead_is_empty(color, board, current_row, current_col):
            moves = Helpers.update_valid_moves(moves, current_row-1, current_col)
        if Pawn._first_move_and_two_squares_ahead_is_empty(color, board, current_row, current_col) and Pawn._one_square_ahead_is_empty(color, board, current_row, current_col): 
            moves = Helpers.update_valid_moves(moves, current_row-2, current_col)
        if Pawn._right_diagonal_take_is_valid(current_col) and Pawn._immediate_right_diagonal_contains_opponent_piece(color, board, current_row, current_col):
            moves = Pawn._get_updated_valid_moves_including_skipped_piece_for_right_diagonal_take(color, board, moves, current_row, current_col)
        if Pawn._left_diagonal_take_is_valid(current_col) and Pawn._immediate_left_diagonal_contains_opponent_piece(color, board, current_row, current_col):
            moves = Pawn._get_updated_valid_moves_including_skipped_piece_for_left_diagonal_take(color, board, moves, current_row, current_col)
      if color == WHITE:
        if Pawn._one_square_ahead_is_empty(color, board, current_row, current_col):
            moves = Helpers.update_valid_moves(moves, current_row+1, current_col)
        if Pawn._first_move_and_two_squares_ahead_is_empty(color, board, current_row, current_col) and Pawn._one_square_ahead_is_empty(color, board, current_row, current_col): 
            moves = Helpers.update_valid_moves(moves, current_row+2, current_col)
        if Pawn._right_diagonal_take_is_valid(current_col) and Pawn._immediate_right_diagonal_contains_opponent_piece(color, board, current_row, current_col):
            moves = Pawn._get_updated_valid_moves_including_skipped_piece_for_right_diagonal_take(color, board, moves, current_row, current_col)
        if Pawn._left_diagonal_take_is_valid(current_col) and Pawn._immediate_left_diagonal_contains_opponent_piece(color, board, current_row, current_col):
            moves = Pawn._get_updated_valid_moves_including_skipped_piece_for_left_diagonal_take(color, board, moves, current_row, current_col)
          
      return moves

    def _one_square_ahead_is_empty(color, board, current_row, current_col):
      if color == BLACK:
        if board[current_row-1][current_col] == 0:
          return True
      if color == WHITE:
        if board[current_row+1][current_col] == 0:
          return True
      return False

    def _first_move_and_two_squares_ahead_is_empty(color, board, current_row, current_col):
      if color == BLACK:
        if current_row == 6 and board[current_row-2][current_col] == 0:
          return True
      else:
        if current_row == 1 and board[current_row+2][current_col] == 0:
          return True
        return False

    def _immediate_right_diagonal_contains_opponent_piece(color, board, current_row, current_col):
      if color == BLACK:
        if board[current_row-1][current_col+1] != 0 and board[current_row-1][current_col+1].color == WHITE:
          return True
      else:
        if board[current_row+1][current_col+1] != 0 and board[current_row+1][current_col+1].color == BLACK:
          return True
      return False

    def _immediate_left_diagonal_contains_opponent_piece(color, board, current_row, current_col):
      if color == BLACK:
        if board[current_row-1][current_col-1] != 0 and board[current_row-1][current_col-1].color == WHITE:
          return True
      else:
        if board[current_row+1][current_col-1] != 0 and board[current_row+1][current_col-1].color == BLACK:
          return True
      return False
    
    def _right_diagonal_take_is_valid(current_col):
      if current_col != 7:
        return True
      return False

    def _left_diagonal_take_is_valid(current_col):
      if current_col != 0:
        return True
      return False

    def _get_updated_valid_moves_including_skipped_piece_for_right_diagonal_take(color, board, moves, current_row, current_col):
      if color == BLACK:
        moves[(current_row-1, current_col+1)] = [board[current_row-1][current_col+1]]
      else:
        moves[(current_row+1, current_col+1)] = [board[current_row+1][current_col+1]]
      return moves

    def _get_updated_valid_moves_including_skipped_piece_for_left_diagonal_take(color, board, moves, current_row, current_col):
      if color == BLACK:
        moves[(current_row-1, current_col-1)] = [board[current_row-1][current_col-1]]
      else:
        moves[(current_row+1, current_col-1)] = [board[current_row+1][current_col-1]]
      return moves



