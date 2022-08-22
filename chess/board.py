import pygame
from .constants import BLACK, ROWS, RED, BLUE, SQUARE_SIZE, COLS, WHITE

class Board:
    def __init__(self, pawn):
        self.board = []
        self.pawn = pawn
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.__create_board()
    
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
    
    def get_piece(self, row, col): 
        return self.board[row][col]

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLUE:
                    self.red_left -= 1
                else:
                    self.white_left -= 1
        
    def get_valid_moves(self, piece):
        moves = {}

        row = piece.row
        col = piece.col
        board = self.board
        
        if piece.type == "PAWN":
          moves = self.__get_valid_pawn_moves(board, row, col, piece)

        return moves

    def draw(self, win):
      self.__draw_squares(win)
      for row in range(ROWS):
          for col in range(COLS):
              piece = self.board[row][col]
              if piece != 0:
                  piece.draw(win)

    def __create_board(self):
      for row in range(ROWS):
          self.board.append([])
          for col in range(COLS):
              if row == 1:
                  self.board[row].append(self.pawn(row, col, WHITE, "PAWN"))
              elif row == 6:
                  self.board[row].append(self.pawn(row, col, BLUE, "PAWN"))
              else:
                  self.board[row].append(0)

    def __draw_squares(self, win):
      win.fill(BLACK)
      for row in range(ROWS):
          for col in range(row % 2, COLS, 2):
              pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Below methods reach into pawn.py
    def __get_valid_pawn_moves(self, board, row, col, piece):
      color = piece.color
      return self.pawn.get_valid_pawn_moves(self, board, row, col, color)

