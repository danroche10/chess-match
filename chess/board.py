from distutils.file_util import move_file
import pygame
from .constants import BLACK, LIGHT_GREY, ROWS, RED, SQUARE_SIZE, COLS, WHITE

class Board:
    def __init__(self, piece_factory):
        self.board = []
        self.potential_check_board = []
        self.piece_factory = piece_factory
        self.__create_board()
    
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
    
    def get_piece(self, row, col): 
        return self.board[row][col]

    def remove(self, pieces):
        self.board[pieces[0].row][pieces[0].col] = 0
        
    def get_valid_moves(self, piece):
        moves = {}
        row = piece.row
        col = piece.col
        board = self.board
        
        if piece.type == "PAWN":
          potential_moves = self.__get_valid_pawn_moves(board, row, col, piece)
          for key in potential_moves:
            if self.this_moves_player_into_check(piece, key[0], key[1]):
              del potential_moves[key]
              moves = potential_moves
          moves = potential_moves     
        elif piece.type == "ROOK":
          moves = self.__get_valid_rook_moves(board, row, col, piece)
        elif piece.type == "BISHOP":
          moves = self.__get_valid_bishop_moves(board, row, col, piece)
        elif piece.type == "QUEEN":
          moves = self.__get_valid_queen_moves(board, row, col, piece)
        elif piece.type == "KNIGHT":
          moves = self.__get_valid_knight_moves(board, row, col, piece)
        elif piece.type == "KING":
          moves = self.__get_valid_king_moves(board, row, col, piece)
        
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
                  elif col == 1 or col == 6:
                      self.board[row].append(self.piece_factory.new_knight(row, col, WHITE))
                  elif col == 2 or col == 5:
                      self.board[row].append(self.piece_factory.new_bishop(row, col, WHITE))
                  elif col == 3:
                      self.board[row].append(self.piece_factory.new_queen(row, col, WHITE))
                  elif col == 4:
                      self.board[row].append(self.piece_factory.new_king(row, col, WHITE))
                  else:
                      self.board[row].append(0)
              elif row == 1:
                  self.board[row].append(self.piece_factory.new_pawn(row, col, WHITE))
              elif row == 6:
                  self.board[row].append(self.piece_factory.new_pawn(row, col, BLACK))
              elif row == 7:
                  if col == 0 or col == 7:
                      self.board[row].append(self.piece_factory.new_rook(row, col, BLACK))
                  elif col == 1 or col == 6:
                      self.board[row].append(self.piece_factory.new_knight(row, col, BLACK))
                  elif col == 2 or col == 5:
                      self.board[row].append(self.piece_factory.new_bishop(row, col, BLACK))
                  elif col == 3:
                      self.board[row].append(self.piece_factory.new_queen(row, col, BLACK))
                  elif col == 4:
                      self.board[row].append(self.piece_factory.new_king(row, col, BLACK))
                  else:
                      self.board[row].append(0)
              else:
                  self.board[row].append(0)

    def __draw_squares(self, win):
      win.fill(LIGHT_GREY)
      for row in range(ROWS):
          for col in range(row % 2, COLS, 2):
              pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Below methods reach into piece extension methods
    # check logic
    def is_opponent_in_check(self, color):
      valid_moves_for_one_color = self.get_all_valid_moves_for_one_colour(color)
      for valid_move in valid_moves_for_one_color:
        if self.potential_check_board[valid_move[0]][valid_move[1]] != 0 and self.potential_check_board[valid_move[0]][valid_move[1]].get_type() == "KING":
          return True
      return False
    
    def get_all_valid_moves_for_one_colour(self, color):
        valid_moves = []
        for row in range(ROWS):
          for col in range(COLS):
            if self.potential_check_board[row][col] != 0 and self.potential_check_board[row][col].get_color() == color:
              if self.potential_check_board[row][col].get_type() == "PAWN":
                  valid_pawn_moves = list(self.__get_valid_pawn_moves(self.potential_check_board, row, col, self.potential_check_board[row][col]).keys())
                  for move in valid_pawn_moves:
                    valid_moves.append(move)
              elif self.board[row][col].get_type() == "ROOK":
                  valid_rook_moves = list(self.__get_valid_rook_moves(self.potential_check_board, row, col, self.board[row][col]).keys())
                  for move in valid_rook_moves:
                    valid_moves.append(move)
              elif self.board[row][col].get_type() == "KNIGHT":
                  valid_knight_moves = list(self.__get_valid_knight_moves(self.board, row, col, self.board[row][col]).keys())
                  for move in valid_knight_moves:
                    valid_moves.append(move)
              elif self.board[row][col].get_type() == "BISHOP":
                  valid_bishop_moves = list(self.__get_valid_bishop_moves(self.board, row, col, self.board[row][col]).keys())
                  for move in valid_bishop_moves:
                    valid_moves.append(move)
              elif self.board[row][col].get_type() == "KING":
                  valid_king_moves = list(self.__get_valid_king_moves(self.board, row, col, self.board[row][col]).keys())
                  for move in valid_king_moves:
                    valid_moves.append(move)
              elif self.board[row][col].get_type() == "QUEEN":
                  valid_queen_moves = list(self.__get_valid_queen_moves(self.board, row, col, self.board[row][col]).keys())
                  for move in valid_queen_moves:
                    valid_moves.append(move)
          
        return valid_moves
    
    def this_moves_player_into_check(self, piece, row, col):
        self.potential_check_board = self.board.copy()
        moving_piece = copy.copy(piece)
        self.potential_check_board[moving_piece.row][moving_piece.col], self.potential_check_board[row][col] = self.potential_check_board[row][col], self.potential_check_board[moving_piece.row][moving_piece.col]
        if (piece.get_color() == BLACK):
          return self.is_opponent_in_check(WHITE)
        else:
          return self.is_opponent_in_check(BLACK)
    
    def __get_valid_pawn_moves(self, board, row, col, piece):
        color = piece.get_color()
        return self.board[row][col].get_valid_pawn_moves(board, row, col, color)     
    
    def __get_valid_rook_moves(self, board, row, col, piece):
        color = piece.color
        return self.board[row][col].get_valid_rook_moves(board, row, col, color)

    def __get_valid_bishop_moves(self, board, row, col, piece):
        color = piece.color
        return self.board[row][col].get_valid_bishop_moves(board, row, col, color)
    
    def __get_valid_queen_moves(self, board, row, col, piece):
        color = piece.color
        return self.board[row][col].get_valid_queen_moves(board, row, col, color)
    
    def __get_valid_knight_moves(self, board, row, col, piece):
        color = piece.color
        return self.board[row][col].get_valid_knight_moves(board, row, col, color)

    def __get_valid_king_moves(self, board, row, col, piece):
        color = piece.color
        return self.board[row][col].get_valid_king_moves(board, row, col, color)   


