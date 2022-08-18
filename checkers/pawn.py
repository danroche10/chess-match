from checkers.helpers import Helpers
from checkers.piece import Piece
from .constants import BLUE, WHITE

class Pawn(Piece):
    def getName():
        return "PAWN"

    def get_valid_pawn_moves(board, row, col, piece):
      moves = {}
      if piece.color == BLUE:
        if Pawn._one_square_ahead_is_empty(piece, board, row, col):
            moves = Helpers.get_updated_valid_moves(moves, row-1, col)
        if Pawn._blues_first_move_and_two_squares_ahead_is_empty(board, row, col): 
            moves = Helpers.get_updated_valid_moves(moves, row-2, col)
        if Pawn._right_diagonal_take_is_valid(col) and Pawn._immediate_right_diagonal_contains_opponent_piece(piece, board, row, col) and board[row-2][col+2] == 0:
            moves[(row-2, col+2)] = [board[row-1][col+1]]
        if Pawn._left_diagonal_take_is_valid(col) and Pawn._immediate_left_diagonal_contains_opponent_piece(piece, board, row, col) and board[row-2][col-2] == 0:
              moves[(row-2, col-2)] = [board[row-1][col-1]]
      if piece.color == WHITE:
        if Pawn._one_square_ahead_is_empty(piece, board, row, col):
            moves = Helpers.get_updated_valid_moves(moves, row+1, col)
        if row == 1 and board[row+2][col] == 0: 
            moves = Helpers.get_updated_valid_moves(moves, row+2, col)
        if Pawn._right_diagonal_take_is_valid(col) and Pawn._immediate_right_diagonal_contains_opponent_piece(piece, board, row, col) and board[row+2][col+2] == 0:
            moves[(row+2, col+2)] = [board[row+1][col+1]]
        if Pawn._left_diagonal_take_is_valid(col) and Pawn._immediate_left_diagonal_contains_opponent_piece(piece, board, row, col) and board[row+2][col-2] == 0:
            moves[(row+2, col-2)] = [board[row+1][col-1]]
          
      return moves

    def _one_square_ahead_is_empty(piece, board, row, col):
      if piece.color == BLUE:
        if board[row-1][col] == 0:
          return True
      if piece.color == WHITE:
        if board[row+1][col] == 0:
          return True
      return False

    def _blues_first_move_and_two_squares_ahead_is_empty(board, row, col):
      if row == 6 and board[row-2][col] == 0:
        return True
      return False

    def _immediate_right_diagonal_contains_opponent_piece(piece, board, row, col):
      if piece.color == BLUE:
        if board[row-1][col+1] != 0 and board[row-1][col+1].color == WHITE:
          return True
      else:
        if board[row+1][col+1] != 0 and board[row+1][col+1].color == BLUE:
          return True
      return False

    def _immediate_left_diagonal_contains_opponent_piece(piece, board, row, col):
      if piece.color == BLUE:
        if board[row-1][col-1] != 0 and board[row-1][col-1].color == WHITE:
          return True
      else:
        if board[row+1][col-1] != 0 and board[row+1][col-1].color == BLUE:
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



