import pytest
from chess.constants import BLACK
from chess.piece import Piece

@pytest.fixture
def new_piece():
  piece = Piece(6, 3, BLACK, "PAWN")
  return piece

def test_type(new_piece):
    assert  new_piece.type == "PAWN"

def test_move(new_piece):
    new_piece.move(4, 3)
    new_row = new_piece.row
    new_col = new_piece.col
    assert new_row == 4
    assert new_col == 3

