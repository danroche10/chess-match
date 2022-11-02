import pygame
from chess.piece import Piece
import pygame
from chess.helpers import Helpers
from chess.piece import Piece
from .constants import BLACK, WHITE

class King(Piece):

    this_is_first_move = True

    def set_this_is_first_move_to_false(self):
        self.this_is_first_move = False
    
    def get_is_first_move(self):
        return self.this_is_first_move
        
    def create(self, win, row, col):
        if self.get_color() == BLACK:
          win.blit(pygame.image.load('chess/assets/black_king.png'), (col*100, row*100))
        else:
          win.blit(pygame.image.load('chess/assets/white_king.png'), (col*100, row*100))

    def get_valid_king_moves(self, board, current_row, current_col, color):
        moves = {}
        if self.get_is_first_move() == True and board[current_row][current_col+1] == 0 and board[current_row][current_col+2] == 0 and board[current_row][current_col+2] != 0 and board[current_row][current_col+2].get_is_first_move():
            moves = Helpers.update_valid_moves(moves, current_row, current_col+2)
        if self.get_is_first_move() == True and board[current_row][current_col-1] == 0 and board[current_row][current_col-2] == 0 and board[current_row][current_col-3] == 0 and board[current_row][current_col-4] !=0 and board[current_row][current_col-4].get_is_first_move():
            moves = Helpers.update_valid_moves(moves, current_row, current_col-3)   
        if current_col <= 6:
            if board[current_row][current_col+1] == 0:
                moves = Helpers.update_valid_moves(moves, current_row, current_col+1)
            elif (board[current_row][current_col+1].get_color() == WHITE and color == BLACK) or (board[current_row][current_col+1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row, current_col+1)
                moves[(current_row, current_col+1)] = [board[current_row][current_col+1]]
        if current_col >=1:
            if board[current_row][current_col-1] == 0:
                moves = Helpers.update_valid_moves(moves, current_row, current_col-1)
            elif (board[current_row][current_col-1].get_color() == WHITE and color == BLACK) or (board[current_row][current_col-1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row, current_col)
                moves[(current_row, current_col-1)] = [board[current_row][current_col-1]]
        if current_row <= 6:
            if board[current_row+1][current_col] == 0:
                moves = Helpers.update_valid_moves(moves, current_row+1, current_col)
            elif (board[current_row+1][current_col].get_color() == WHITE and color == BLACK) or (board[current_row+1][current_col].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row+1, current_col)
                moves[(current_row+1, current_col)] = [board[current_row+1][current_col]]
        if current_row >= 1:
            if board[current_row-1][current_col] == 0:
                moves = Helpers.update_valid_moves(moves, current_row-1, current_col)
            elif (board[current_row-1][current_col].get_color() == WHITE and color == BLACK) or (board[current_row-1][current_col].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row-1, current_col)
                moves[(current_row-1, current_col)] = [board[current_row-1][current_col]]
        if current_row >= 1 and current_col >= 1:
            if board[current_row-1][current_col-1] == 0:
                moves = Helpers.update_valid_moves(moves, current_row-1, current_col-1)
            elif (board[current_row-1][current_col-1].get_color() == WHITE and color == BLACK) or (board[current_row-1][current_col-1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row-1, current_col-1)
                moves[(current_row-1, current_col-1)] = [board[current_row-1][current_col-1]]
        if current_row >= 1 and current_col <= 6:
            if board[current_row-1][current_col+1] == 0:
                moves = Helpers.update_valid_moves(moves, current_row-1, current_col+1)
            elif (board[current_row-1][current_col+1].get_color() == WHITE and color == BLACK) or (board[current_row-1][current_col+1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row-1, current_col+1)
                moves[(current_row-1, current_col+1)] = [board[current_row-1][current_col+1]]
        if current_row <= 6 and current_col <= 6:
            if board[current_row+1][current_col+1] == 0:
                moves = Helpers.update_valid_moves(moves, current_row+1, current_col+1)
            elif (board[current_row+1][current_col+1].get_color() == WHITE and color == BLACK) or (board[current_row+1][current_col+1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row+1, current_col+1)
                moves[(current_row+1, current_col+1)] = [board[current_row+1][current_col+1]]
        if current_row <= 6 and current_col >= 1:
            if board[current_row+1][current_col-1] == 0:
                moves = Helpers.update_valid_moves(moves, current_row+1, current_col-1)
            elif (board[current_row+1][current_col-1].get_color() == WHITE and color == BLACK) or (board[current_row+1][current_col-1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, current_row+1, current_col-1)
                moves[(current_row-1, current_col-1)] = [board[current_row+1][current_col-1]]
        
        return moves