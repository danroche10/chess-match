import pygame
from chess.helpers import Helpers
from chess.piece import Piece
from .constants import BLACK, WHITE

class Knight(Piece):
    def create(self, win, row, col):
        if self.get_color() == BLACK:
          win.blit(pygame.image.load('chess/assets/black_knight.png'), (col*100, row*100))
        else:
          win.blit(pygame.image.load('chess/assets/white_knight.png'), (col*100, row*100))

    def get_valid_knight_moves(self, board, current_row, current_col, color):
        moves = {}

        self._up_two_right_one_moves(moves, board, current_row, current_col, color)        
        self._up_two_left_one_moves(moves, board, current_row, current_col, color)
        self._down_two_right_one_moves(moves, board, current_row, current_col, color)
        self._down_two_left_one_moves(moves, board, current_row, current_col, color)
        self._left_two_up_one_moves(moves, board, current_row, current_col, color)
        self._right_two_down_one_moves(moves, board, current_row, current_col, color)
        self._right_two_up_one_moves(moves, board, current_row, current_col, color) 
        self._left_two_down_one_moves(moves, board, current_row, current_col, color)
        
        return moves


    def _up_two_right_one_moves(self, moves, board, current_row, current_col, color):
        if current_col <= 6 and current_row >= 2:
            if board[current_row-2][current_col+1] == 0:
                moves = Helpers.update_valid_moves(moves, current_row-2, current_col+1)
            elif (board[current_row-2][current_col+1].get_color() == WHITE and color == BLACK) or (board[current_row-2][current_col+1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row-2, current_col+1)
                moves[(current_row-2, current_col+1)] = [board[current_row-2][current_col+1]]
    
    def _up_two_left_one_moves(self, moves, board, current_row, current_col, color):
        if current_col >= 1 and current_row >= 2:
            if board[current_row-2][current_col-1] == 0:
                moves = Helpers.update_valid_moves(moves, current_row-2, current_col-1)
            elif (board[current_row-2][current_col-1].get_color() == WHITE and color == BLACK) or (board[current_row-2][current_col-1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row-2, current_col-1)
                moves[(current_row-2, current_col-1)] = [board[current_row-2][current_col-1]]

    def _down_two_right_one_moves(self, moves, board, current_row, current_col, color):
        if current_col <=6 and current_row <= 5:
            if board[current_row+2][current_col+1] == 0:
                moves = Helpers.update_valid_moves(moves, current_row+2, current_col+1)
            elif (board[current_row+2][current_col+1].get_color() == WHITE and color == BLACK) or (board[current_row+2][current_col+1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row, current_col)
                moves[(current_row+2, current_col+1)] = [board[current_row+2][current_col+1]]
    
    def _down_two_left_one_moves(self, moves, board, current_row, current_col, color):
        if current_col >= 1 and current_row <= 5:
            if board[current_row+2][current_col-1] == 0:
                moves = Helpers.update_valid_moves(moves, current_row+2, current_col-1)
            elif (board[current_row+2][current_col-1].get_color() == WHITE and color == BLACK) or (board[current_row+2][current_col-1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row+2, current_col-1)
                moves[(current_row+2, current_col-1)] = [board[current_row+2][current_col-1]]

    def _left_two_up_one_moves(self, moves, board, current_row, current_col, color):
        if current_col >= 2 and current_row >= 1:
            if board[current_row-1][current_col-2] == 0:
                moves = Helpers.update_valid_moves(moves, current_row-1, current_col-2)
            elif (board[current_row-1][current_col-2].get_color() == WHITE and color == BLACK) or (board[current_row-1][current_col-2].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row-1, current_col-2)
                moves[(current_row-1, current_col-2)] = [board[current_row-1][current_col-2]]

    def _right_two_down_one_moves(self, moves, board, current_row, current_col, color):
        if current_col <=5 and current_row <= 6:
            if board[current_row+1][current_col+2] == 0:
                moves = Helpers.update_valid_moves(moves, current_row+1, current_col+2)
            elif (board[current_row+1][current_col+2].get_color() == WHITE and color == BLACK) or (board[current_row+1][current_col+2].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row+1, current_col+2)
                moves[(current_row+1, current_col+2)] = [board[current_row+1][current_col+2]]
    
    def _right_two_up_one_moves(self, moves, board, current_row, current_col, color):
        if current_col <= 5 and current_row >= 1:
            if board[current_row-1][current_col+2] == 0:
                moves = Helpers.update_valid_moves(moves, current_row-1, current_col+2)
            elif (board[current_row-1][current_col+2].get_color() == WHITE and color == BLACK) or (board[current_row-1][current_col+2].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row-1, current_col+2)
                moves[(current_row-1, current_col+2)] = [board[current_row-1][current_col+2]]
    
    def _left_two_down_one_moves(self, moves, board, current_row, current_col, color):
        if current_col >= 2 and current_row <= 6:
            if board[current_row+1][current_col-2] == 0:
                moves = Helpers.update_valid_moves(moves, current_row+1, current_col-2)
            elif (board[current_row+1][current_col-2].get_color() == WHITE and color == BLACK) or (board[current_row+1][current_col-2].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row+1, current_col-2)
                moves[(current_row+1, current_col-2)] = [board[current_row+1][current_col-2]]