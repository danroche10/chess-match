import pygame
from .constants import BLACK, ROWS, RED, BLUE, SQUARE_SIZE, COLS, WHITE
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()
    
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == 1:
                    self.board[row].append(Piece(row, col, WHITE))
                elif row == 6:
                    self.board[row].append(Piece(row, col, BLUE))
                else:
                    self.board[row].append(0)
  
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLUE:
                    self.red_left -= 1
                else:
                    self.white_left -= 1
    
    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return BLUE
        
        return None 
    
    def get_valid_moves(self, piece):
        moves = {}

        row = piece.row
        col = piece.col

        if piece.color == BLUE:
            if self.board[row-1][col] == 0:
                moves[(row-1, col)] = []
            if row == 6 and self.board[row-2][col] == 0: 
                moves[(row-2, col)] = []
                # include color below
            if self.board[row-1][col+1] != 0 and self.board[row-2][col+2] == 0 and self.board[row-1][col+1].color == WHITE:
                moves[(row-2, col+2)] = [self.board[row-1][col+1]]
            if self.board[row-1][col-1] != 0 and self.board[row-2][col-2] == 0 and self.board[row-1][col-1].color == WHITE:
                moves[(row-2, col-2)] = [self.board[row-1][col-1]]
        if piece.color == WHITE:
            if self.board[row-1][col] == 0:
                moves[(row+1, col)] = []
            if row == 1 and self.board[row+2][col] == 0: 
                moves[(row+2, col)] = []
            if self.board[row+1][col+1] != 0 and self.board[row+2][col+2] == 0 and self.board[row+1][col+1].color == BLUE:
                moves[(row+2, col+2)] = [self.board[row+1][col+1]]
            if self.board[row+1][col-1] != 0 and self.board[row+2][col-2] == 0 and self.board[row+1][col-1].color == BLUE:
                moves[(row+2, col-2)] = [self.board[row+1][col-1]]
        
        return moves