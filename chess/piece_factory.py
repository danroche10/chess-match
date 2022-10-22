from .constants import WHITE
from chess.pawn import Pawn

class PieceFactory:
  def new_pawn(row, col, color):
    return Pawn(row, col, color, "PAWN")