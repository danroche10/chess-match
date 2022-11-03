import pygame
from chess.helpers import Helpers
from chess.piece import Piece
from .constants import BLACK, WHITE

class Rook(Piece):
    this_is_first_move = True

    def set_this_is_first_move_to_false(self):
        self.this_is_first_move = False
    
    def get_is_first_move(self):
        return self.this_is_first_move
    
    def create(self, win, row, col):
        if self.get_color() == BLACK:
          win.blit(pygame.image.load('chess/assets/black_rook.png'), (col*100, row*100))
        else:
          win.blit(pygame.image.load('chess/assets/white_rook.png'), (col*100, row*100))

    def get_valid_rook_moves(self, board, current_row, current_col, color):
        moves = {}

        potential_move_current_row = current_row
        potential_move_current_col = current_col
        self._get_horizontal_rook_moves(moves, board, potential_move_current_col, current_row, current_col, color)
        self._get_vertical_rook_moves(moves, board, potential_move_current_row, current_row, current_col, color)
            
        return moves
    
    def _get_horizontal_rook_moves(self, moves, board, potential_move_current_col, current_row, current_col, color):
        self._get_horizontal_moves_to_right(moves, board, current_row, current_col, potential_move_current_col, color)
        self._get_horizontal_moves_to_left(moves, board, current_row, current_col, potential_move_current_col, color)

    def _get_vertical_rook_moves(self, moves, board, potential_move_current_row, current_row, current_col, color):
        self._get_vertical_moves_down(moves, board, current_row, current_col, potential_move_current_row, color)
        self._get_vertical_moves_up(moves, board, current_row, current_col, potential_move_current_row, color)
    
    def _get_horizontal_moves_to_right(self, moves, board, current_row, current_col, potential_move_current_col, color):
        while potential_move_current_col <= 7:
            potential_move_current_col += 1
            if potential_move_current_col == 8:
                break
            elif board[current_row][potential_move_current_col] == 0:
                moves = Helpers.update_valid_moves(moves, current_row, potential_move_current_col)
            elif (board[current_row][potential_move_current_col].get_color() == WHITE and color == BLACK) or (board[current_row][potential_move_current_col].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row, potential_move_current_col)
                moves[(current_row, potential_move_current_col)] = [board[current_row][potential_move_current_col]]
                break
            elif (board[current_row][current_col].get_color() == BLACK and color == BLACK) or (board[current_row][current_col].get_color() == WHITE and color == WHITE):
                break
        potential_move_current_col = current_col

    def _get_horizontal_moves_to_left(self, moves, board, current_row, current_col, potential_move_current_col, color):
        while potential_move_current_col >= 0:
            potential_move_current_col -= 1
            if potential_move_current_col == -1:
                break
            elif board[current_row][potential_move_current_col] == 0:
                moves = Helpers.update_valid_moves(moves, current_row, potential_move_current_col)
            elif (board[current_row][potential_move_current_col].get_color() == WHITE and color == BLACK) or (board[current_row][potential_move_current_col].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row, potential_move_current_col)
                moves[(current_row, potential_move_current_col)] = [board[current_row][potential_move_current_col]]
                break
            elif (board[current_row][potential_move_current_col].get_color() == BLACK and color == BLACK) or (board[current_row][potential_move_current_col].get_color() == WHITE and color == WHITE):
                break
        potential_move_current_col = current_col

    
    def _get_vertical_moves_down(self, moves, board, current_row, current_col, potential_move_current_row, color):
        while potential_move_current_row <= 7:
            potential_move_current_row += 1
            if potential_move_current_row == 8:
                break
            elif board[potential_move_current_row][current_col] == 0:
                moves = Helpers.update_valid_moves(moves, potential_move_current_row, current_col)
            elif (board[potential_move_current_row][current_col].get_color() == WHITE and color == BLACK) or (board[potential_move_current_row][current_col].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, potential_move_current_row, current_col)
                break
            elif (board[current_row][current_col].get_color() == BLACK and color == BLACK) or (board[current_row][current_col].get_color() == WHITE and color == WHITE):
                break
        potential_move_current_row = current_row
        

    def _get_vertical_moves_up(self, moves, board, current_row, current_col, potential_move_current_row, color):
        while potential_move_current_row >= 0:
            potential_move_current_row -= 1
            if potential_move_current_row == -1:
                break
            elif board[potential_move_current_row][current_col] == 0:
                moves = Helpers.update_valid_moves(moves, potential_move_current_row, current_col)
            elif (board[potential_move_current_row][current_col].get_color() == WHITE and color == BLACK) or (board[potential_move_current_row][current_col].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, potential_move_current_row, current_col)
                moves[(potential_move_current_row, current_col)] = [board[potential_move_current_row][current_col]]
                break
            elif (board[current_row][current_col].get_color() == BLACK and color == BLACK) or (board[current_row][current_col].get_color() == WHITE and color == WHITE):
                break
        potential_move_current_row = current_row
