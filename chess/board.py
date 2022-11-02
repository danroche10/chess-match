import pygame
import copy
from .constants import BLACK, LIGHT_GREY, ROWS, RED, SQUARE_SIZE, COLS, WHITE

class Board:
    def __init__(self, piece_factory):
        self.board = []
        self.potential_check_board = []
        self.piece_factory = piece_factory
        self.pieces = ["PAWN", "ROOK", "KNIGHT", "BISHOP", "QUEEN", "KING"]
        self.__create_board()
    
    def move(self, piece, row, col):
        if piece.get_type() == "KING" and (col - piece.col == 2):
          self.castle_to_right(piece, row, col)
        elif piece.get_type() == "KING" and (piece.col - col == 3):
          self.castle_to_left(piece, row, col)
        else:
          self.board[piece.row][piece.col], self.board[row][col] = 0, self.get_piece(piece.row, piece.col)
          piece.move(row, col)
        if piece.get_type() == "KING" or piece.get_type() == "ROOK":
          piece.set_this_is_first_move_to_false()
        if piece.get_type() == "PAWN":
          if row == 0:
            self.board[row][col] = self.piece_factory.new_queen(row, col, BLACK)
          elif row == 7: 
            self.board[row][col] = self.piece_factory.new_queen(row, col, WHITE)
        if self.__this_moves_opp_player_into_check(piece, row, col):
          if piece.get_color() == BLACK:
            print("White is in check") 
          else: print("Black is in check")
    
    def get_piece(self, row, col): 
        return self.board[row][col]
    
    def get_piece_from_potential_check_board(self, row, col): 
        return self.potential_check_board[row][col]

    def remove(self, pieces):
        self.board[pieces[0].row][pieces[0].col] = 0
    
    def draw(self, win):
      self.__draw_squares(win)
      for row in range(ROWS):
          for col in range(COLS):
              piece = self.get_piece(row, col)                          
              if piece != 0:
                  piece.create(win, row, col)
    
    # Below methods reach into piece extension methods
    def get_valid_moves(self, piece_to_play):
        moves = {}
        row = piece_to_play.row
        col = piece_to_play.col
        board = self.board
        
        for piece in self.pieces:
          if piece_to_play.get_type() == piece:
            piece_method = f'get_valid_{piece.lower()}_moves'
            potential_moves = getattr(piece_to_play, piece_method)(board, row, col, piece_to_play.get_color())
            for key in potential_moves:
              if self.__this_moves_player_into_check(piece_to_play, key[0], key[1]) == False:
                moves[key] = potential_moves[key]
        return moves
    
    def __is_opponent_in_check(self, color):
        valid_moves_for_one_color = self.__get_all_valid_moves_for_one_colour(color)
        for valid_move in valid_moves_for_one_color:
          if self.get_piece_from_potential_check_board(valid_move[0], valid_move[1]) != 0 and (self.get_piece_from_potential_check_board(valid_move[0], valid_move[1]).get_type() == "KING"):
            if self.get_piece_from_potential_check_board(valid_move[0], valid_move[1]).get_color() != color:
                return True
        return False

    def __is_opponent_in_check_mate(self, color):
        valid_moves = []
        for row in range(ROWS):
          for col in range(COLS):
            if self.get_piece_from_potential_check_board(row, col) != 0 and self.get_piece_from_potential_check_board(row, col).get_color() == color:
              valid_moves.append(self.get_valid_moves(self.get_piece_from_potential_check_board(row, col)))
        
        new_list = [item for item in valid_moves if item]
        if new_list == []:
          print(("Check mate!!"))
          # end game
          return True
        else:
          return False
    
    def __get_all_valid_moves_for_one_colour(self, color):
        valid_moves = []
        for row in range(ROWS):
          for col in range(COLS):
            if self.get_piece_from_potential_check_board(row, col) != 0 and self.get_piece_from_potential_check_board(row, col).get_color() == color:
              for piece in self.pieces:
                if self.get_piece_from_potential_check_board(row, col).get_type() == piece:
                  piece_method = f'get_valid_{piece.lower()}_moves'
                  valid_piece_moves = list(getattr(self.get_piece_from_potential_check_board(row, col), piece_method)(self.potential_check_board, row, col, color))
                  for move in valid_piece_moves:
                      valid_moves.append(move)
        
        return valid_moves

    def __this_moves_player_into_check(self, piece, row, col):
      self.potential_check_board = copy.deepcopy(self.board)
      self.potential_check_board[piece.row][piece.col], self.potential_check_board[row][col]  = 0, self.get_piece_from_potential_check_board(piece.row, piece.col)
      if (piece.get_color() == BLACK):
        return self.__is_opponent_in_check(WHITE)
      else:
        return self.__is_opponent_in_check(BLACK)

    def __this_moves_opp_player_into_check(self, piece, row, col):
      self.potential_check_board = copy.deepcopy(self.board)
      self.potential_check_board[piece.row][piece.col], self.potential_check_board[row][col] = 0, self.get_piece_from_potential_check_board(piece.row, piece.col)
      if (piece.get_color() == BLACK):
        self.__is_opponent_in_check_mate(WHITE)
        return self.__is_opponent_in_check(BLACK)
      else:
        self.__is_opponent_in_check_mate(BLACK)
        return self.__is_opponent_in_check(WHITE)

    def castle_to_right(self, piece, row, col):
        self.board[row][col+1].move(row, col-1)
        self.board[piece.row][piece.col], self.board[row][col] = 0, self.get_piece(piece.row, piece.col)
        piece.move(row, col)
        self.board[row][col+1], self.board[row][col-1] = 0, self.get_piece(row, col+1)
    
    def castle_to_left(self, piece, row, col):
        self.board[row][col-1].move(row, col+1)
        self.board[piece.row][piece.col], self.board[row][col] = 0, self.get_piece(piece.row, piece.col)
        piece.move(row, col)
        self.board[row][col-1], self.board[row][col+1] = 0, self.get_piece(row, col-1)

    # methods for drawing board
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