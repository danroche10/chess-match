from checkers.constants import BLUE

class Helpers:
  def get_updated_valid_moves(moves, row, col):
    moves[(row, col)] = []
    return moves
