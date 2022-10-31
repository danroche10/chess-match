import pygame
from chess.piece import Piece
import pygame
from chess.helpers import Helpers
from chess.piece import Piece
from .constants import BLACK, WHITE

class King(Piece):
    def create(self, win, row, col):
        if self.get_color() == BLACK:
          win.blit(pygame.image.load('chess/assets/black_king.png'), (col*100, row*100))
        else:
          win.blit(pygame.image.load('chess/assets/white_king.png'), (col*100, row*100))

    def get_valid_king_moves(self, board, row, col, color):
        moves = {}
        if col <= 6:
            if board[row][col+1] == 0:
                moves = Helpers.update_valid_moves(moves, row, col+1)
            elif (board[row][col+1].get_color() == WHITE and color == BLACK) or (board[row][col+1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row, col+1)
                moves[(row, col+1)] = [board[row][col+1]]
        if col >=1:
            if board[row][col-1] == 0:
                moves = Helpers.update_valid_moves(moves, row, col-1)
            elif (board[row][col-1].get_color() == WHITE and color == BLACK) or (board[row][col-1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row, col)
                moves[(row, col-1)] = [board[row][col-1]]
        if row <= 6:
            if board[row+1][col] == 0:
                moves = Helpers.update_valid_moves(moves, row+1, col)
            elif (board[row+1][col].get_color() == WHITE and color == BLACK) or (board[row+1][col].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row+1, col)
                moves[(row+1, col)] = [board[row+1][col]]
        if row >= 1:
            if board[row-1][col] == 0:
                moves = Helpers.update_valid_moves(moves, row-1, col)
            elif (board[row-1][col].get_color() == WHITE and color == BLACK) or (board[row-1][col].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row-1, col)
                moves[(row-1, col)] = [board[row-1][col]]
        if row >= 1 and col >= 1:
            if board[row-1][col-1] == 0:
                moves = Helpers.update_valid_moves(moves, row-1, col-1)
            elif (board[row-1][col-1].get_color() == WHITE and color == BLACK) or (board[row-1][col-1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row-1, col-1)
                moves[(row-1, col-1)] = [board[row-1][col-1]]
        if row >= 1 and col <= 6:
            if board[row-1][col+1] == 0:
                moves = Helpers.update_valid_moves(moves, row-1, col+1)
            elif (board[row-1][col+1].get_color() == WHITE and color == BLACK) or (board[row-1][col+1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row-1, col+1)
                moves[(row-1, col+1)] = [board[row-1][col+1]]
        if row <= 6 and col <= 6:
            if board[row+1][col+1] == 0:
                moves = Helpers.update_valid_moves(moves, row+1, col+1)
            elif (board[row+1][col+1].get_color() == WHITE and color == BLACK) or (board[row+1][col+1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row+1, col+1)
                moves[(row+1, col+1)] = [board[row+1][col+1]]
        if row <= 6 and col >= 1:
            if board[row+1][col-1] == 0:
                moves = Helpers.update_valid_moves(moves, row+1, col-1)
            elif (board[row+1][col-1].get_color() == WHITE and color == BLACK) or (board[row+1][col-1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row+1, col-1)
                moves[(row-1, col-1)] = [board[row+1][col-1]]
        
        return moves