from chess.pawn import Pawn
from chess.rook import Rook

class PieceFactory:
  def new_pawn(row, col, color):
    return Pawn(row, col, color, "PAWN")
  def new_rook(row, col, color):
    return Rook(row, col, color, "ROOK")