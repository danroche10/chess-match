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

    def get_valid_knight_moves(self, board, row, col, color):
        moves = {}
        if col <= 6 and row >= 2:
            if board[row-2][col+1] == 0:
                moves = Helpers.update_valid_moves(moves, row-2, col+1)
            elif (board[row-2][col+1].get_color() == WHITE and color == BLACK) or (board[row-2][col+1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row-2, col+1)
                moves[(row-2, col+1)] = [board[row-2][col+1]]
        if col <=6 and row <= 5:
            if board[row+2][col+1] == 0:
                moves = Helpers.update_valid_moves(moves, row+2, col+1)
            elif (board[row+2][col+1].get_color() == WHITE and color == BLACK) or (board[row+2][col+1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row, col)
                moves[(row+2, col+1)] = [board[row+2][col+1]]
        if col >= 1 and row >= 2:
            if board[row-2][col-1] == 0:
                moves = Helpers.update_valid_moves(moves, row-2, col-1)
            elif (board[row-2][col-1].get_color() == WHITE and color == BLACK) or (board[row-2][col-1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row-2, col-1)
                moves[(row-2, col-1)] = [board[row-2][col-1]]
        if col >= 1 and row <= 5:
            if board[row+2][col-1] == 0:
                moves = Helpers.update_valid_moves(moves, row+2, col-1)
            elif (board[row+2][col-1].get_color() == WHITE and color == BLACK) or (board[row+2][col-1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row+2, col-1)
                moves[(row+2, col-1)] = [board[row+2][col-1]]
        #here
        if col >= 2 and row <= 6:
            if board[row+1][col-2] == 0:
                moves = Helpers.update_valid_moves(moves, row+1, col-2)
            elif (board[row+1][col-2].get_color() == WHITE and color == BLACK) or (board[row+1][col-2].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row+1, col-2)
                moves[(row+1, col-2)] = [board[row+1][col-2]]
        if col <=5 and row <= 6:
            if board[row+1][col+2] == 0:
                moves = Helpers.update_valid_moves(moves, row+1, col+2)
            elif (board[row+1][col+2].get_color() == WHITE and color == BLACK) or (board[row+1][col+2].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row+1, col+2)
                moves[(row+1, col+2)] = [board[row+1][col+2]]
        if col >= 2 and row >= 1:
            if board[row-1][col-2] == 0:
                moves = Helpers.update_valid_moves(moves, row-1, col-2)
            elif (board[row-1][col-2].get_color() == WHITE and color == BLACK) or (board[row-1][col-2].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_valid_moves(moves, row-2, col-1)
                moves[(row-1, col-2)] = [board[row-1][col-2]]
        if col <= 5 and row >= 1:
            if board[row-1][col+2] == 0:
                moves = Helpers.update_valid_moves(moves, row-1, col+2)
            elif (board[row-1][col+2].get_color() == WHITE and color == BLACK) or (board[row-1][col+1].get_color() == BLACK and color == WHITE):
                moves = Helpers.update_moves_valid_moves(moves, row+2, col-1)
                moves[(row-1, col+2)] = [board[row-1][col+2]]
        
        return moves