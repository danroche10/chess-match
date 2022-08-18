class Helpers:
  def get_updated_valid_moves(moves, row, col):
    moves[(row, col)] = []
    return moves

  def get_updated_valid_moves_included_skipped_piece(board, moves, row, col):
    moves[(row, col)] = [board[row][col]]
    return moves
