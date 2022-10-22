from chess.pawn import Pawn
from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King

class PieceFactory:
  def new_pawn(row, col, color):
    return Pawn(row, col, color, "PAWN")
  
  def new_rook(row, col, color):
    return Rook(row, col, color, "ROOK")
  
  def new_knight(row, col, color):
    return Knight(row, col, color, "KNIGHT")
  
  def new_bishop(row, col, color):
    return Bishop(row, col, color, "BISHOP")
  
  def new_queen(row, col, color):
    return Queen(row, col, color, "Queen")
  
  def new_king(row, col, color):
    return King(row, col, color, "King")