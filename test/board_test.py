from unittest.mock import Mock
import pytest
from chess.board import Board

@pytest.fixture
def new_board():
    pawn = Mock()
    board = Board(pawn)
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
    blue_piece = board.get_piece(6,3)
    blue_piece.row, blue_piece.col = 6, 3
    board.move(blue_piece, 4, 3)
    blue_piece.row, blue_piece.col = 4, 3
    board.remove([blue_piece])
    piece_in_blues_previous_position = board.get_piece(4, 3)
    assert piece_in_blues_previous_position == 0

def test_get_valid_moves(new_board):
    board = new_board
    blue_piece = board.get_piece(6,3)
    blue_piece.row, blue_piece.col = 6, 3
    blue_piece.type = "PAWN"
    board.__get_valid_pawn_moves.assert_called_with(board, 6, 3, blue_piece)
  




