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

    def get_valid_pawn_moves(self, board, row, col, color):
      moves = {}
      if color == BLACK:
        if Pawn._one_square_ahead_is_empty(color, board, row, col):
            moves = Helpers.update_valid_moves(moves, row-1, col)
        if Pawn._first_move_and_two_squares_ahead_is_empty(color, board, row, col): 
            moves = Helpers.update_valid_moves(moves, row-2, col)
        if Pawn._right_diagonal_take_is_valid(col) and Pawn._immediate_right_diagonal_contains_opponent_piece(color, board, row, col) and Pawn._landing_square_for_right_diagonal_take_is_empty(color, board, row, col):
            moves = Pawn._update_valid_moves_including_skipped_piece_for_right_diagonal_take(color, board, moves, row, col)
        if Pawn._left_diagonal_take_is_valid(col) and Pawn._immediate_left_diagonal_contains_opponent_piece(color, board, row, col) and Pawn._landing_square_for_left_diagonal_take_is_empty(color, board, row, col):
            moves = Pawn._update_valid_moves_including_skipped_piece_for_left_diagonal_take(color, board, moves, row, col)
      if color == WHITE:
        if Pawn._one_square_ahead_is_empty(color, board, row, col):
            moves = Helpers.update_valid_moves(moves, row+1, col)
        if Pawn._first_move_and_two_squares_ahead_is_empty(color, board, row, col): 
            moves = Helpers.update_valid_moves(moves, row+2, col)
        if Pawn._right_diagonal_take_is_valid(col) and Pawn._immediate_right_diagonal_contains_opponent_piece(color, board, row, col) and Pawn._landing_square_for_right_diagonal_take_is_empty(color, board, row, col):
            moves = Pawn._update_valid_moves_including_skipped_piece_for_right_diagonal_take(color, board, moves, row, col)
        if Pawn._left_diagonal_take_is_valid(col) and Pawn._immediate_left_diagonal_contains_opponent_piece(color, board, row, col) and Pawn._landing_square_for_left_diagonal_take_is_empty(color, board, row, col):
            moves = Pawn._update_valid_moves_including_skipped_piece_for_left_diagonal_take(color, board, moves, row, col)
          
      return moves

    def _one_square_ahead_is_empty(color, board, row, col):
      if color == BLACK:
        if board[row-1][col] == 0:
          return True
      if color == WHITE:
        if board[row+1][col] == 0:
          return True
      return False

    def _first_move_and_two_squares_ahead_is_empty(color, board, row, col):
      if color == BLACK:
        if row == 6 and board[row-2][col] == 0:
          return True
      else:
        if row == 1 and board[row+2][col] == 0:
          return True
        return False

    def _immediate_right_diagonal_contains_opponent_piece(color, board, row, col):
      if color == BLACK:
        if board[row-1][col+1] != 0 and board[row-1][col+1].color == WHITE:
          return True
      else:
        if board[row+1][col+1] != 0 and board[row+1][col+1].color == BLACK:
          return True
      return False

    def _immediate_left_diagonal_contains_opponent_piece(color, board, row, col):
      if color == BLACK:
        if board[row-1][col-1] != 0 and board[row-1][col-1].color == WHITE:
          return True
      else:
        if board[row+1][col-1] != 0 and board[row+1][col-1].color == BLACK:
          return True
      return False
    
    def _right_diagonal_take_is_valid(col):
      if col != 6 and col != 7:
        return True
      return False

    def _left_diagonal_take_is_valid(col):
      if col != 0 and col != 1:
        return True
      return False

    def _get_updated_valid_moves_including_skipped_piece_for_right_diagonal_take(color, board, moves, row, col):
      if color == BLACK:
        moves[(row-2, col+2)] = [board[row-1][col+1]]
      else:
        moves[(row+2, col+2)] = [board[row+1][col+1]]
      return moves

    def _get_updated_valid_moves_including_skipped_piece_for_left_diagonal_take(color, board, moves, row, col):
      if color == BLACK:
        moves[(row-2, col-2)] = [board[row-1][col-1]]
      else:
        moves[(row+2, col-2)] = [board[row+1][col-1]]
      return moves
      
    def _landing_square_for_right_diagonal_take_is_empty(color, board, row, col):
      if color == BLACK:
        if board[row-2][col+2] == 0:
          return True
      else:
        if board[row+2][col+2] == 0:
          return True
      return False

    def _landing_square_for_left_diagonal_take_is_empty(color, board, row, col):
      if color == BLACK:
        if board[row-2][col-2] == 0:
          return True
      else:
        if board[row+2][col-2] == 0:
          return True
      return False





