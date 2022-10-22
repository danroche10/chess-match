from unittest.mock import MagicMock, Mock
import pytest
from chess.board import Board

@pytest.fixture
def new_board():
    pawn = Mock()
    board = Board(pawn)
    pawn.get_valid_pawn_moves = MagicMock(return_value={(4,3): []})
    return board

def test_get_piece(new_board):
    board = new_board
    piece = board.get_piece(1,1)
    assert piece != 0

def test_move(new_board):
    board = new_board
    piece = board.get_piece(1,1)
    piece.row, piece.col = 1, 1
    board.move(piece, 3, 1)
    piece_in_new_location = board.get_piece(3,1)
    assert piece_in_new_location == piece

def test_remove(new_board):
    board = new_board
    black_piece = board.get_piece(6,3)
    black_piece.row, black_piece.col = 6, 3
    board.move(black_piece, 4, 3)
    black_piece.row, black_piece.col = 4, 3
    board.remove([black_piece])
    piece_in_blacks_previous_position = board.get_piece(4, 3)
    assert piece_in_blacks_previous_position == 0

def test_get_valid_moves(new_board):
    board = new_board
    black_piece = board.get_piece(6,3)
    black_piece.type = "PAWN"
    valid_moves = board.get_valid_moves(black_piece)
    assert valid_moves == {(4,3): []}
  




