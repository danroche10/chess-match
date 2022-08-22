from unittest.mock import MagicMock, Mock
import pytest
from chess.pawn import Pawn
from chess.constants import ROWS, COLS, WHITE, BLUE

@pytest.fixture
def new_board():
    board = []
    for row in range(ROWS):
        board.append([])
        for col in range(COLS):
            if row == 1:
                board[row].append(Pawn(row, col, BLUE, "PAWN"))
            elif row == 6:
                board[row].append(Pawn(row, col, BLUE, "PAWN"))
            else:
                board[row].append(0)
    return board

def test_get_valid_pawn_moves_1(new_board):
    pawn_to_move = new_board[6][3]
    row = pawn_to_move.row
    col = pawn_to_move.col
    color = pawn_to_move.color
    valid_pawn_moves = pawn_to_move.get_valid_pawn_moves(new_board, row, col, color)
    assert valid_pawn_moves == {(4,3) : [], (5,3) : []}