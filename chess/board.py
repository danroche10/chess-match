import pygame
from .constants import BLACK, LIGHT_GREY, ROWS, RED, SQUARE_SIZE, COLS, WHITE

class Board:
    def __init__(self, piece_factory):
        self.board = []
        self.piece_factory = piece_factory
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
                if piece.get_color() == BLACK:
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
                  piece.create(win, row, col)

    def __create_board(self):
      for row in range(ROWS):
          self.board.append([])
          for col in range(COLS):
              if row == 0:
                  if col == 0 or col == 7:
                      self.board[row].append(self.piece_factory.new_rook(row, col, WHITE))
                  else:
                      self.board[row].append(0)
              elif row == 1:
                  self.board[row].append(self.piece_factory.new_pawn(row, col, WHITE))
              elif row == 6:
                  self.board[row].append(self.piece_factory.new_pawn(row, col, BLACK))
              elif row == 7:
                  if col == 0 or col == 7:
                      self.board[row].append(self.piece_factory.new_rook(row, col, BLACK))
                  else:
                      self.board[row].append(0)
              else:
                  self.board[row].append(0)

    def __draw_squares(self, win):
      win.fill(LIGHT_GREY)
      for row in range(ROWS):
          for col in range(row % 2, COLS, 2):
              pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Below methods reach into pawn.py
    def __get_valid_pawn_moves(self, board, row, col, piece):
      color = piece.color
      return self.board[row][col].get_valid_pawn_moves(board, row, col, color)

