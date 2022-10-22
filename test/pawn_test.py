from unittest.mock import MagicMock, Mock
import pytest
from chess.pawn import Pawn
from chess.constants import ROWS, COLS, WHITE, BLACK

@pytest.fixture
def new_board():
    board = []
    for row in range(ROWS):
        board.append([])
        for col in range(COLS):
            if row == 1:
                board[row].append(Pawn(row, col, WHITE, "PAWN"))
            elif row == 6:
                board[row].append(Pawn(row, col, BLACK, "PAWN"))
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
  
def test_get_valid_pawn_moves_2(new_board):
    # change board setup
    new_board[6][3] = 0
    new_board[1][4] = 0
    pawn_to_take = new_board[4][3] = Pawn(4, 3, BLACK, "PAWN")
    pawn_to_get_taken = new_board[3][4] = Pawn(3, 4, WHITE, "PAWN")
    row = pawn_to_take.row
    col = pawn_to_take.col
    color = pawn_to_take.color
    valid_pawn_moves = pawn_to_take.get_valid_pawn_moves(new_board, row, col, color)
    assert valid_pawn_moves == {(3,3) : [], (2,5) : [pawn_to_get_taken]}