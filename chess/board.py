import pygame
import copy
from .constants import BLACK, LIGHT_GREY, ROWS, RED, SQUARE_SIZE, COLS, WHITE, PIECE_TYPES

class Board:
    def __init__(self, piece_factory):
        self.board, self.potential_check_board = [], []
        self.piece_factory = piece_factory
        self.piece_types = PIECE_TYPES
        self.__create_board()
    
    def move(self, piece_to_move, destination_row, destination_col):
        if self.__player_is_castling_to_right(piece_to_move, destination_col):
          self.__castle_to_right(piece_to_move, destination_row, destination_col)
        elif self.__player_is_castling_to_left(piece_to_move, destination_col):
          self.__castle_to_left(piece_to_move, destination_row, destination_col)
        else:
          self.__standard_move(piece_to_move, destination_row, destination_col)
        self.__make_any_relevant_updates_following_move(piece_to_move, destination_row, destination_col)
    
    def get_piece(self, row, col): 
        return self.board[row][col]
    
    def get_piece_from_potential_check_board(self, row, col): 
        return self.potential_check_board[row][col]

    def remove(self, piece):
        self.board[piece[0].row][piece[0].col] = 0
    
    def draw(self, win):
      self.__draw_squares(win)
      for row in range(ROWS):
          for col in range(COLS):
              piece = self.get_piece(row, col)                          
              if piece != 0:
                  piece.create(win, row, col)
    
    # Below methods reach into piece extension methods
    def get_valid_moves(self, piece_to_play):
        valid_moves = {}
        destination_row, destination_col = piece_to_play.row, piece_to_play.col
        
        for piece in self.piece_types:
          if piece_to_play.get_type() == piece:
            piece_method = f'get_valid_{piece.lower()}_moves'
            potential_moves = getattr(piece_to_play, piece_method)(self.board, destination_row, destination_col, piece_to_play.get_color())
            self.__validate_moves_that_do_not_put_player_in_check(piece_to_play, potential_moves, valid_moves)
        return valid_moves
    
    def __validate_moves_that_do_not_put_player_in_check(self, piece_to_move, potential_moves, valid_moves):
        for potential_move in potential_moves:
          potential_move_destination_row = potential_move[0]
          potential_move_destination_col = potential_move[1]
          if piece_to_move.get_type() == "KING" and (potential_move_destination_col - piece_to_move.col == 2):
            if self.__this_moves_player_into_check(piece_to_move, potential_move_destination_row, potential_move_destination_col-1) == False and self.__this_moves_player_into_check(piece_to_move, potential_move_destination_row, potential_move_destination_col) == False:
              valid_moves[potential_move] = potential_moves[potential_move]
          elif piece_to_move.get_type() == "KING" and (piece_to_move.col - potential_move_destination_col == 3):
            if self.__this_moves_player_into_check(piece_to_move, potential_move_destination_row, potential_move_destination_col+1) == False and self.__this_moves_player_into_check(piece_to_move, potential_move_destination_row, potential_move_destination_col+2) == False and self.__this_moves_player_into_check(piece_to_move, potential_move_destination_row, potential_move_destination_col) == False:
              valid_moves[potential_move] = potential_moves[potential_move]
          elif piece_to_move.get_type() and self.__this_moves_player_into_check(piece_to_move, potential_move_destination_row, potential_move_destination_col) == False:
            valid_moves[potential_move] = potential_moves[potential_move]
    
    def __notify_players_of_check(self, piece_to_move):
        if piece_to_move.get_color() == BLACK:
          print("White is in check") 
        else: print("Black is in check")
  
    def __standard_move(self, piece_to_move, destination_row, destination_col):
      self.board[piece_to_move.row][piece_to_move.col], self.board[destination_row][destination_col] = 0, self.get_piece(piece_to_move.row, piece_to_move.col)
      piece_to_move.move(destination_row, destination_col)
    
    def __is_opponent_in_check(self, color_to_play):
        valid_moves_for_one_color = self.__get_all_valid_moves_for_one_colour(color_to_play)
        for valid_move in valid_moves_for_one_color:
          valid_move_desination_row, valid_move_destination_col = valid_move[0], valid_move[1]
          if self.get_piece_from_potential_check_board(valid_move_desination_row, valid_move_destination_col) != 0 and (self.get_piece_from_potential_check_board(valid_move_desination_row, valid_move_destination_col).get_type() == "KING"):
            if self.get_piece_from_potential_check_board(valid_move_desination_row, valid_move_destination_col).get_color() != color_to_play:
                return True
        return False

    def __is_opponent_in_check_mate(self, color_to_play):
        valid_moves = []
        for valid_move_destination_row in range(ROWS):
          for valid_move_destination_col in range(COLS):
            if self.get_piece_from_potential_check_board(valid_move_destination_row, valid_move_destination_col) != 0 and self.get_piece_from_potential_check_board(valid_move_destination_row, valid_move_destination_col).get_color() == color_to_play:
              valid_moves.append(self.get_valid_moves(self.get_piece_from_potential_check_board(valid_move_destination_row, valid_move_destination_col)))
        
        valid_moves_with_empty_dicts_removed = [valid_move for valid_move in valid_moves if valid_move]
        if valid_moves_with_empty_dicts_removed == []:
          return True
        else:
          return False
    
    def __get_all_valid_moves_for_one_colour(self, color):
        valid_moves = []
        for valid_move_destination_row in range(ROWS):
          for valid_move_destination_col in range(COLS):
            if self.get_piece_from_potential_check_board(valid_move_destination_row, valid_move_destination_col) != 0 and self.get_piece_from_potential_check_board(valid_move_destination_row, valid_move_destination_col).get_color() == color:
                self.__get_valid_moves_for_each_piece_type(valid_moves, valid_move_destination_row, valid_move_destination_col, color)
        
        return valid_moves

    def __get_valid_moves_for_each_piece_type(self, valid_moves, valid_move_destination_row, valid_move_destination_col, color):
        for piece_type in self.piece_types:
          if self.get_piece_from_potential_check_board(valid_move_destination_row, valid_move_destination_col).get_type() == piece_type:
              get_valid_x_moves_method = f'get_valid_{piece_type.lower()}_moves'
              valid_piece_moves = list(getattr(self.get_piece_from_potential_check_board(valid_move_destination_row, valid_move_destination_col), get_valid_x_moves_method)(self.potential_check_board, valid_move_destination_row, valid_move_destination_col, color))
              for move in valid_piece_moves:
                  valid_moves.append(move)
        
        return valid_moves

    def __this_moves_player_into_check(self, piece_to_move, destination_row, destination_col):
      self.potential_check_board = copy.deepcopy(self.board)
      self.potential_check_board[piece_to_move.row][piece_to_move.col], self.potential_check_board[destination_row][destination_col]  = 0, self.get_piece_from_potential_check_board(piece_to_move.row, piece_to_move.col)
      if (piece_to_move.get_color() == BLACK):
        return self.__is_opponent_in_check(WHITE)
      else:
        return self.__is_opponent_in_check(BLACK)

    def __this_moves_opp_player_into_check(self, piece_to_move, destination_row, destination_col):
      self.potential_check_board = copy.deepcopy(self.board)
      self.potential_check_board[piece_to_move.row][piece_to_move.col], self.potential_check_board[destination_row][destination_col] = 0, self.get_piece_from_potential_check_board(piece_to_move.row, piece_to_move.col)
      if (piece_to_move.get_color() == BLACK):
         if self.__is_opponent_in_check(BLACK):
            if self.__is_opponent_in_check_mate(WHITE):
              print("checkmate!!")
              return
            return True
      else:
         if self.__is_opponent_in_check(BLACK):
            if self.__is_opponent_in_check_mate(WHITE):
              print("checkmate!!")
              return
            return True

    def __make_any_relevant_updates_following_move(self, piece_to_move, destination_row, destination_col):
      if piece_to_move.get_type() == "KING" or piece_to_move.get_type() == "ROOK":
        piece_to_move.set_this_is_first_move_to_false()
      if piece_to_move.get_type() == "PAWN" and (destination_row == 0 or destination_row == 7):
        self.__promote_pawn(self, destination_row, destination_col)
      if self.__this_moves_opp_player_into_check(piece_to_move, destination_row, destination_col):
        self.__notify_players_of_check(piece_to_move)
    
    def __player_is_castling_to_right(self, piece_to_move, destination_col):
       return piece_to_move.get_type() == "KING" and (destination_col - piece_to_move.col == 2)

    def __player_is_castling_to_left(self, piece_to_move, destination_col):
       return piece_to_move.get_type() == "KING" and (piece_to_move.col - destination_col == 3)

    def __castle_to_right(self, king_to_move, destination_row, destination_col):
        rook_to_move = self.get_piece(destination_row, destination_col+1)
        rook_to_move.move(destination_row, destination_col-1)
        self.board[king_to_move.row][king_to_move.col], self.board[destination_row][destination_col] = 0, king_to_move
        king_to_move.move(destination_row, destination_col)
        self.board[destination_row][destination_col+1], self.board[destination_row][destination_col-1] = 0, rook_to_move
    
    def __castle_to_left(self, king_to_move, destination_row, destination_col):
        rook_to_move = self.board[destination_row][destination_col-1]
        rook_to_move.move(destination_row, destination_col+1)
        self.board[king_to_move.row][king_to_move.col], self.board[destination_row][destination_col] = 0, king_to_move
        king_to_move.move(destination_row, destination_col)
        self.board[destination_row][destination_col-1], self.board[destination_row][destination_col+1] = 0, rook_to_move
    
    def __promote_pawn(self, destination_row, destination_col):
        if destination_row == 0:
            self.board[destination_row][destination_col] = self.piece_factory.new_queen(destination_row, destination_col, BLACK)
        elif destination_row == 7: 
            self.board[destination_row][destination_col] = self.piece_factory.new_queen(destination_row, destination_col, WHITE)

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