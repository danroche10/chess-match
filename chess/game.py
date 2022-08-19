import pygame
from .constants import WHITE, BLUE, SQUARE_SIZE

class Game:
    def __init__(self, win, board):
        self.__init(board)
        self.win = win
    
    def update(self):
        self.__draw_board(self.win)
        self.__draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def __init(self, board):
        self.selected = None
        self.board = board
        self.turn = BLUE
        self.valid_moves = {}

    def select(self, row, col):
        if self.selected:
            result = self.__move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.__get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.__get_valid_moves(piece)
            return True
            
        return False

    def __move(self, row, col):
        piece = self.__get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.__move_piece_to_new_square(self.selected, row, col)
            skipped_piece = self.valid_moves[(row, col)]
            if skipped_piece:
                self.__remove_piece_from_board(skipped_piece)
            self.__change_turn()
        else:
            return False
        return True

    def __draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def __change_turn(self):
        self.valid_moves = {}
        if self.turn == BLUE:
            self.turn = WHITE
        else:
            self.turn = BLUE
    
    # Below methods reach into board.py
    def __get_piece(self, row, col):
      return self.board.get_piece(row, col)

    def __get_valid_moves(self, piece):
      return self.board.get_valid_moves(piece)

    def __remove_piece_from_board(self, skipped_piece):
      return self.board.remove(skipped_piece)

    def __move_piece_to_new_square(self, piece, row, col):
      return self.board.move(piece, row, col)

    def __draw_board(self, win):
      self.board.draw(win)